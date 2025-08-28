# scrape_craigslist_ohio.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import random
import re
import pandas as pd
from datetime import datetime
import logging

# --- Configuration ---

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Base headers to mimic a browser
BASE_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

# Ohio cities to scrape (Craigslist subdomains)
# Verified against https://geo.craigslist.org/iso/us/oh
OHIO_CITIES = [
    'columbus', 'cincinnati', 'cleveland', 'toledo', 'akron',
    'dayton', 'youngstown', 'canton', 'lorain', 'hamilton',
    'springfield', 'kettering', 'mason', 'beavercreek', 'fairfield',
    'middletown', 'newark', 'cuyahoga', 'delaware', 'summit',
    'lake', 'geauga', 'portage', 'stark', 'butler', 'warren',
    'montgomery', 'franklin', 'clark', ' Greene' # Add more as needed
]

# Filters
MAX_PRICE = 600000
REQUIRED_KEYWORDS = [] # Keywords that must be in title/description (optional)
EXCLUDED_KEYWORDS = [
    'auction', 'condo', 'new construction', 'foreclosure',
    'land', 'coming soon', 'business opportunity', 'wanted', 'swap'
] # Keywords to exclude

# Delay settings (seconds)
DELAY_RANGE = (2, 5) # Random delay between requests

# Output files
RESIDENTIAL_CSV = 'Residential_Craigslist_OH.csv'
COMMERCIAL_CSV = 'Commercial_Craigslist_OH.csv'

# --- Helper Functions ---

def _is_valid_price(price_str):
    """Check if price string is valid and under MAX_PRICE."""
    if not price_str:
        return False
    try:
        # Remove non-numeric characters except decimal point
        clean_price = re.sub(r'[^\d.]', '', price_str)
        price = float(clean_price)
        return price > 0 and price <= MAX_PRICE
    except (ValueError, TypeError):
        return False

def _contains_excluded_keywords(text):
    """Check if text contains any excluded keywords."""
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in EXCLUDED_KEYWORDS)

def _contains_required_keywords(text):
    """Check if text contains all required keywords (if any)."""
    if not REQUIRED_KEYWORDS:
        return True # No required keywords means pass
    if not text:
        return False
    text_lower = text.lower()
    return all(keyword in text_lower for keyword in REQUIRED_KEYWORDS)

def _classify_property_type(title, description, attributes_text):
    """Classify property type based on title, description, and attributes."""
    combined_text = f"{title} {description} {attributes_text}".lower()

    # Check for commercial indicators first
    commercial_indicators = [
        'office', 'retail', 'industrial', 'commercial', 'warehouse',
        'restaurant', 'hotel', 'motels', 'shopping center', 'business',
        'storefront', 'shop', 'salon', 'clinic'
    ]
    if any(word in combined_text for word in commercial_indicators):
        return 'Commercial'

    # Check for multifamily indicators
    multifamily_indicators = [
        'duplex', 'triplex', 'quadplex', 'multi family', 'multi-family',
        'apartment building', 'units', 'rental units'
    ]
    if any(word in combined_text for word in multifamily_indicators):
        return 'Multifamily'

    # Check for SFH indicators
    sfh_indicators = [
        'house', 'home', 'single family', 'sfh', 'cottage', 'bungalow', 'ranch'
    ]
    if any(word in combined_text for word in sfh_indicators):
        return 'SFH'

    # Default to SFH if it seems residential and not clearly commercial/multifamily
    residential_indicators = ['bedroom', 'bathroom', 'br', 'ba', 'sqft', 'ft2']
    if any(word in combined_text for word in residential_indicators) and not _contains_excluded_keywords(combined_text):
         return 'SFH' # Assume SFH if it has residential specs and isn't excluded

    return 'Unknown' # Cannot classify

def _extract_contact_info(text):
    """Extract potential phone numbers and emails from text (basic)."""
    phones = set() # Use set to avoid duplicates
    emails = set()

    if text:
        # Find phone numbers (various formats)
        phone_matches = re.findall(r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})', text)
        phones.update(phone_matches)

        # Find email addresses
        email_matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        emails.update(email_matches)

    return '; '.join(sorted(phones)), '; '.join(sorted(emails))

# --- Scraping Logic ---

def scrape_craigslist_listing(session, listing_url):
    """
    Scrape details from a single Craigslist listing page.
    """
    logger.debug(f"Scraping listing: {listing_url}")
    try:
        time.sleep(random.uniform(*DELAY_RANGE)) # Be respectful
        response = session.get(listing_url, headers=BASE_HEADERS, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        data = {
            'source': 'Craigslist',
            'listing_url': listing_url,
            'property_address': '',
            'asking_price': '',
            'property_type': 'Unknown',
            'agent_phone': 'N/A',
            'agent_email': 'N/A',
            'owner_phone': '',
            'owner_email': '',
            'number_of_units': 'N/A', # Usually not directly available for SFH
            'year_built': 'N/A', # Usually not directly available
            'water_expense': 'N/A',
            'electricity_expense': 'N/A',
            'lawn_care_expense': 'N/A',
            'gas_expense': 'N/A',
            'snow_removal_expense': 'N/A',
            'property_taxes_expense': 'N/A',
            'other_expenses': 'N/A',
            'gross_rental_income': 'N/A',
            'current_cash_flow': 'N/A',
            'current_cap_rate': 'N/A',
            'nearest_school_rating': 'N/A',
            'title': '',
            'description': '',
            'bedrooms': '',
            'bathrooms': '',
            'square_footage': '',
            'date_posted': '',
            'days_on_market': '', # Will calculate if date_posted is available
            'location': '', # City/area from title or map
            'latitude': '',
            'longitude': '',
            'attributes': '' # Text from attrgroup
        }

        # --- Extract data using BeautifulSoup and JSON-LD ---

        # 1. JSON-LD Structured Data (Primary source if available)
        json_scripts = soup.find_all('script', type='application/ld+json')
        for script in json_scripts:
            try:
                import json
                json_data = json.loads(script.string)
                # Handle potential list or single object
                items = json_data if isinstance(json_data, list) else [json_data]
                for item in items:
                    if isinstance(item, dict):
                        if item.get('@type') == 'House':
                            data['asking_price'] = item.get('offers', [{}])[0].get('price', '')
                            # Address
                            addr_info = item.get('address', {})
                            if isinstance(addr_info, dict):
                                locality = addr_info.get('addressLocality', '')
                                region = addr_info.get('addressRegion', '')
                                postal_code = addr_info.get('postalCode', '')
                                country = addr_info.get('addressCountry', '')
                                # Combine into a readable address string
                                parts = [locality, region, postal_code, country]
                                data['property_address'] = ', '.join(part for part in parts if part)

                            data['bedrooms'] = item.get('numberOfBedrooms', '')
                            data['bathrooms'] = item.get('numberOfBathroomsTotal', '')
                            data['latitude'] = item.get('latitude', '')
                            data['longitude'] = item.get('longitude', '')
                            data['title'] = item.get('name', '')
                        # Add logic for other @types if needed (e.g., ApartmentComplex for MF?)
            except (json.JSONDecodeError, TypeError, AttributeError) as e:
                logger.debug(f"Error parsing JSON-LD: {e}")
                continue

        # 2. Title and Price (from main heading)
        title_elem = soup.find('span', id='titletextonly')
        if title_elem:
             data['title'] = title_elem.get_text(strip=True)

        price_elem = soup.find('span', class_='price')
        if price_elem:
            raw_price = price_elem.get_text(strip=True)
            if _is_valid_price(raw_price):
                data['asking_price'] = raw_price
            # If price is invalid, we might skip this listing later

        # 3. Location (from title span or map)
        title_span = soup.find('span', class_='postingtitletext')
        if title_span:
            loc_span = title_span.find('span', string=re.compile(r'\(.*\)'))
            if loc_span:
                data['location'] = loc_span.get_text(strip=True).strip('()')

        map_div = soup.find('div', id='map')
        if map_div:
            data['latitude'] = map_div.get('data-latitude', '')
            data['longitude'] = map_div.get('data-longitude', '')

        # 4. Date Posted
        date_elem = soup.find('time', class_='date timeago')
        if date_elem and date_elem.get('datetime'):
            try:
                from dateutil import parser
                dt_obj = parser.parse(date_elem['datetime'])
                data['date_posted'] = dt_obj.strftime('%Y-%m-%d')
                # Calculate days on market (approximation)
                days_diff = (datetime.now() - dt_obj).days
                data['days_on_market'] = str(days_diff) if days_diff >= 0 else ''
            except Exception as e:
                logger.debug(f"Error parsing date: {e}")

        # 5. Description
        body_elem = soup.find('section', id='postingbody')
        if body_elem:
            # Get text and remove the "QR Code Link..." part if present
            full_text = body_elem.get_text(" ", strip=True)
            qr_index = full_text.find("QR Code Link to This Post")
            if qr_index != -1:
                data['description'] = full_text[:qr_index].strip()
            else:
                data['description'] = full_text

        # 6. Attributes (Beds, Baths, Sqft, Property Type hints)
        attr_groups = soup.find_all('div', class_='attrgroup')
        all_attrs_text = ""
        for group in attr_groups:
            attrs_text = group.get_text(" ", strip=True)
            all_attrs_text += " " + attrs_text
            # Extract specific attributes if easily parseable
            # This is tricky due to varied formats, so we mainly use text for classification
            # Example: <span class="attr important"> 3BR / 2Ba </span>
            # Example: <span class="attr important"> 1280ft<sup>2</sup> </span>
            if 'BR' in attrs_text and 'Ba' in attrs_text:
                 # Rough extraction
                 br_match = re.search(r'(\d+)\s*BR', attrs_text)
                 ba_match = re.search(r'(\d+(?:\.\d+)?)\s*Ba', attrs_text)
                 sqft_match = re.search(r'(\d+(?:,\d+)?)\s*ft2?', attrs_text)
                 if br_match:
                     data['bedrooms'] = br_match.group(1)
                 if ba_match:
                     data['bathrooms'] = ba_match.group(1)
                 if sqft_match:
                     data['square_footage'] = sqft_match.group(1)

        data['attributes'] = all_attrs_text.strip()

        # 7. Classify Property Type
        data['property_type'] = _classify_property_type(data['title'], data['description'], data['attributes'])

        # 8. Extract Contact Info (from description text)
        # Note: Direct contact info is often hidden behind a "show contact" link.
        # This extracts what's directly visible in the ad text.
        full_text_for_contact = f"{data['title']} {data['description']} {data['attributes']}"
        phone_str, email_str = _extract_contact_info(full_text_for_contact)
        # Assign to owner for now, as it's user-posted
        data['owner_phone'] = phone_str
        data['owner_email'] = email_str
        # Agent fields are less likely to be directly posted, mark as N/A or leave blank
        # unless specific broker info is found (rare on CL)

        # 9. Basic Validation based on filters
        # Exclude if price is invalid or contains excluded keywords
        if not _is_valid_price(data['asking_price']) or \
           _contains_excluded_keywords(f"{data['title']} {data['description']} {data['attributes']}"):
            logger.debug(f"Listing excluded based on filters: {listing_url}")
            return None # Skip this listing

        # Classify as Unknown if type couldn't be determined and it's not explicitly excluded
        if data['property_type'] == 'Unknown':
             logger.debug(f"Could not classify property type for: {listing_url}")
             # You might choose to skip unknown types or include them for manual review
             # For now, let's include them but flag them
             pass

        logger.info(f"Successfully scraped: {data['title'][:50]}...")
        return data

    except requests.RequestException as e:
        logger.error(f"Request error for {listing_url}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error scraping {listing_url}: {e}", exc_info=True)
    return None # Return None on any error


def scrape_craigslist_search_results(session, search_url):
    """
    Scrape listing URLs from a Craigslist search results page.
    Handles pagination.
    """
    listing_urls = []
    current_url = search_url
    page_count = 0
    max_pages = 5 # Limit pages to prevent infinite loops for now

    while current_url and page_count < max_pages:
        page_count += 1
        logger.info(f"Scraping search results page {page_count}: {current_url}")
        try:
            time.sleep(random.uniform(*DELAY_RANGE)) # Be respectful
            response = session.get(current_url, headers=BASE_HEADERS, timeout=20)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # --- NEW (Corrected) Logic for Updated CL Structure ---
            logger.debug("Attempting to parse search results with updated selectors...")

            # Find all gallery cards (each represents a listing)
            gallery_cards = soup.find_all('div', class_='gallery-card')

            page_links_found = 0
            for card in gallery_cards:
                # Find the link using the more specific anchor class
                # The primary link is often the one with class 'posting-title' or just the main link within the card
                # Let's target the 'cl-search-anchor' which seems specific to search results
                link_tag = card.find('a', class_='cl-search-anchor') # More specific class
                if not link_tag:
                    # Fallback 1: Find any link within the card that has an href
                    link_tag = card.find('a', href=True)

                if link_tag and link_tag.get('href'):
                    full_url = urljoin(search_url, link_tag['href'])
                    # Basic de-duplication
                    if full_url not in listing_urls:
                        listing_urls.append(full_url)
                        page_links_found += 1
                        logger.debug(f"Found listing URL: {full_url}")

            logger.debug(f"Found {page_links_found} listing URLs on page {page_count} using new selectors.")

            # --- Finding the Next Page Link (also updated) ---
            # Find next page link - look for pagination controls
            next_page_link = None
            pagination_container = soup.find('div', class_='paginator') # Common container
            if not pagination_container:
                pagination_container = soup.find('div', {'aria-label': 'Pagination'}) # Alternative

            if pagination_container:
                # Look for the "next" button/link
                next_btn = pagination_container.find('a', string=re.compile(r'next', re.I)) # Case insensitive 'next'
                if next_btn and next_btn.get('href'):
                    next_page_link = urljoin(search_url, next_btn['href'])
                    logger.debug(f"Found next page link: {next_page_link}")
                else:
                    # If no 'next' button, try to find numbered page links and pick the next one
                    # This is trickier, but a basic approach:
                    # Find the current page marker (if any) and the link after it
                    # This part might need refinement based on exact structure
                    # Placeholder for now - rely on 'next' button
                    pass
            else:
                # Alternative method if no paginator div found
                # Sometimes it's just a link with specific text or class
                 next_btn_alt = soup.find('a', class_='button next') # Older class pattern
                 if not next_btn_alt:
                     next_btn_alt = soup.find('a', string='Next') # Plain text
                 if next_btn_alt and next_btn_alt.get('href'):
                    next_page_link = urljoin(search_url, next_btn_alt['href'])
                    logger.debug(f"Found next page link (alt method): {next_page_link}")

            # --- END NEW Logic ---

            if next_page_link and next_page_link != current_url:
                current_url = next_page_link
                # Add a slightly longer delay before fetching the next page
                time.sleep(random.uniform(DELAY_RANGE[0], DELAY_RANGE[1] * 2))
            else:
                logger.info("No more pages found or reached max pages.")
                break

        except requests.RequestException as e:
            logger.error(f"Request error for search page {current_url}: {e}")
            break # Stop on request error
        except Exception as e:
            logger.error(f"Unexpected error scraping search page {current_url}: {e}", exc_info=True)
            break # Stop on unexpected error

    logger.info(f"Finished scraping search results. Total unique listing URLs found: {len(listing_urls)}")
    return listing_urls


def main():
    """
    Main function to orchestrate the scraping process.
    """
    logger.info("Starting Craigslist Ohio Real Estate Scraper...")

    all_scraped_data = []
    session = requests.Session() # Reuse connection

    for city in OHIO_CITIES:
        logger.info(f"--- Scraping city: {city} ---")
        try:
            # Base URL for the city's real estate section
            # We'll search for "real estate" listings, which often includes "by owner" and "by broker"
            base_search_url = f"https://{city}.craigslist.org/search/rea"

            # Scrape the search results to get listing URLs
            listing_urls = scrape_craigslist_search_results(session, base_search_url)

            if not listing_urls:
                logger.warning(f"No listing URLs found for city {city}.")
                continue

            # Scrape details for each listing URL
            city_listings_scraped = 0
            for url in listing_urls:
                listing_data = scrape_craigslist_listing(session, url)
                if listing_data: # Check if listing_data is not None
                    all_scraped_data.append(listing_data)
                    city_listings_scraped += 1
                    # Optional: Print progress
                    if city_listings_scraped % 10 == 0:
                        logger.info(f"Scraped {city_listings_scraped} listings for {city} so far...")

            logger.info(f"Finished scraping {city}. Listings scraped: {city_listings_scraped}")

        except Exception as e:
            logger.error(f"Error processing city {city}: {e}", exc_info=True)
            continue # Continue with the next city

    logger.info(f"Scraping complete. Total listings scraped: {len(all_scraped_data)}")

    if not all_scraped_data:
        logger.warning("No data was scraped. Exiting.")
        return

    # --- Process and Export Data ---

    # Convert to DataFrame
    df = pd.DataFrame(all_scraped_data)

    # Filter out 'Unknown' property types if desired, or handle them separately
    # df = df[df['property_type'] != 'Unknown']

    # Map property types to sheets
    residential_df = df[df['property_type'].isin(['SFH', 'Multifamily'])].copy()
    commercial_df = df[df['property_type'] == 'Commercial'].copy()

    # --- Prepare Data for CSV Export (Matching Task Requirements) ---

    # Helper to safely convert price strings to floats
    def clean_price(price_str):
        if not price_str:
            return ""
        try:
            # Remove currency symbols and commas
            clean_str = re.sub(r'[^\d.]', '', str(price_str))
            if clean_str:
                return float(clean_str)
        except (ValueError, TypeError):
            pass
        return ""

    # Residential Sheet Mapping
    residential_data = []
    for _, row in residential_df.iterrows():
        residential_data.append({
            "Property Address": row.get('property_address', ''),
            "Asking Price": clean_price(row.get('asking_price', '')),
            "Property Type (SFH/Multifamily/Commercial)": row.get('property_type', ''),
            "Agent Phone Number / Agent Email": f"{row.get('agent_phone', 'N/A')} / {row.get('agent_email', 'N/A')}".strip(' / '),
            "Owner Phone / Owner Email": f"{row.get('owner_phone', '')} / {row.get('owner_email', '')}".strip(' / '),
            "Number of Units": row.get('number_of_units', 'N/A'), # Often N/A for SFH
            "Year Built": row.get('year_built', 'N/A'),
            "Water": row.get('water_expense', 'N/A'),
            "Electricity": row.get('electricity_expense', 'N/A'),
            "Lawn Care": row.get('lawn_care_expense', 'N/A'),
            "Gas": row.get('gas_expense', 'N/A'),
            "Snow Removal": row.get('snow_removal_expense', 'N/A'),
            "Property Taxes": row.get('property_taxes_expense', 'N/A'),
            "Other": row.get('other_expenses', 'N/A'),
            "Current Gross Rental Income": row.get('gross_rental_income', 'N/A'),
            "Current Cash Flow": row.get('current_cash_flow', 'N/A'),
            "Current Cap Rate (NOI / Purchase Price)": row.get('current_cap_rate', 'N/A'),
            "Nearest High School Zillow Zip Code Rating": row.get('nearest_school_rating', 'N/A')
            # Add other fields from row if needed for debugging (url, title, etc.)
        })

    # Commercial Sheet Mapping
    commercial_data = []
    for _, row in commercial_df.iterrows():
         commercial_data.append({
            "Property Address": row.get('property_address', ''),
            "Asking Price": clean_price(row.get('asking_price', '')),
            "Property Type (SFH/Multifamily/Commercial)": row.get('property_type', ''),
            "Agent Phone Number / Agent Email": f"{row.get('agent_phone', 'N/A')} / {row.get('agent_email', 'N/A')}".strip(' / '),
            "Owner Phone / Owner Email": f"{row.get('owner_phone', '')} / {row.get('owner_email', '')}".strip(' / '),
            "Number of Units": row.get('number_of_units', 'N/A'),
            "Year Built": row.get('year_built', 'N/A'),
            "Water": row.get('water_expense', 'N/A'),
            "Electricity": row.get('electricity_expense', 'N/A'),
            "Lawn Care": row.get('lawn_care_expense', 'N/A'),
            "Gas": row.get('gas_expense', 'N/A'),
            "Snow Removal": row.get('snow_removal_expense', 'N/A'),
            "Property Taxes": row.get('property_taxes_expense', 'N/A'),
            "Other": row.get('other_expenses', 'N/A'),
            "Current Gross Rental Income": row.get('gross_rental_income', 'N/A'),
            "Current Cash Flow": row.get('current_cash_flow', 'N/A'),
            "Current Cap Rate (NOI / Purchase Price)": row.get('current_cap_rate', 'N/A'),
            "Nearest High School Zillow Zip Code Rating": row.get('nearest_school_rating', 'N/A')
            # Add other fields from row if needed for debugging
        })

    # --- Export to CSV ---
    # Ensure columns are in the correct order if needed, or just use the dict keys
    columns_order = [
        "Property Address", "Asking Price", "Property Type (SFH/Multifamily/Commercial)",
        "Agent Phone Number / Agent Email", "Owner Phone / Owner Email", "Number of Units",
        "Year Built", "Water", "Electricity", "Lawn Care", "Gas", "Snow Removal",
        "Property Taxes", "Other", "Current Gross Rental Income", "Current Cash Flow",
        "Current Cap Rate (NOI / Purchase Price)", "Nearest High School Zillow Zip Code Rating"
    ]

    # Create DataFrames with specified column order
    residential_export_df = pd.DataFrame(residential_data, columns=columns_order)
    commercial_export_df = pd.DataFrame(commercial_data, columns=columns_order)

    # Sort by Cash Flow (descending) - Since Cash Flow is mostly "N/A", this won't rank effectively.
    # If you calculate and store Cash Flow later, you can sort here.
    # residential_export_df.sort_values(by="Current Cash Flow", ascending=False, inplace=True, key=pd.to_numeric, errors='coerce')
    # commercial_export_df.sort_values(by="Current Cash Flow", ascending=False, inplace=True, key=pd.to_numeric, errors='coerce')

    # Add ranking column *after* sorting (if sorting worked)
    # residential_export_df.insert(0, 'Rank', range(1, len(residential_export_df) + 1))
    # commercial_export_df.insert(0, 'Rank', range(1, len(commercial_export_df) + 1))

    # Export to CSV
    residential_export_df.to_csv(RESIDENTIAL_CSV, index=False)
    commercial_export_df.to_csv(COMMERCIAL_CSV, index=False)

    logger.info(f"Exported {len(residential_export_df)} Residential listings to {RESIDENTIAL_CSV}")
    logger.info(f"Exported {len(commercial_export_df)} Commercial listings to {COMMERCIAL_CSV}")
    logger.info("Scraping and export process finished.")

if __name__ == '__main__':
    main()