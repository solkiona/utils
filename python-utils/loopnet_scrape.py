import asyncio
import random
import os
from playwright.async_api import async_playwright
import re # For extracting Listing ID

# --- Configuration ---
# Replace with a working LoopNet search URL that shows results after applying your filters.
# Make sure this URL works when you paste it into your regular Chrome browser.
# Example: TARGET_URL = "https://www.loopnet.com/search/multifamily/oh/for-sale/?propertytype=8&price=0-599999"
TARGET_URL = "https://sandusky.craigslist.org/" # <<< UPDATE THIS

# --- Update these paths for your Linux system ---
username = os.getenv('USER')
if not username:
    raise ValueError("Could not determine Linux username. Is the USER environment variable set?")
CHROME_PATH = "/usr/bin/google-chrome" # Adjust if needed (e.g., /usr/bin/chromium-browser)
USER_DATA_DIR = f"/home/{username}/.config/google-chrome/Profile 2" # Main Chrome config folder
# --- End Configuration ---
print(f"Intended Profile Path: {USER_DATA_DIR}")
async def get_property_data_from_search_page(listing_element):
    """Extracts basic data from a single listing element on the search results page."""
    data = {}
    try:
        # --- Title & Link ---
        # Based on your HTML snippet: <h4><a ...>2265 12th St SW</a></h4>
        title_link_elem = await listing_element.query_selector('h4 a')
        if title_link_elem:
            data['title'] = (await title_link_elem.inner_text()).strip()
            data['link'] = await title_link_elem.get_attribute('href')
            # Ensure absolute URL
            if data['link'] and data['link'].startswith('/'):
                data['link'] = 'https://www.loopnet.com' + data['link']
        else:
            data['title'] = 'N/A'
            data['link'] = 'N/A'

        # --- Address ---
        # Based on your HTML snippet: <a ... class="subtitle-beta">Akron, OH 44314</a>
        address_elem = await listing_element.query_selector('header a.subtitle-beta')
        data['address'] = (await address_elem.inner_text()).strip() if address_elem else 'N/A'

        # --- Key Facts (Price, Type, Size) ---
        # Based on your HTML snippet: <ul class="data-points-2c"> <li>$100.00</li> <li>4 Unit Apartment Building</li> ...
        facts_list = await listing_element.query_selector('div.data ul.data-points-2c')
        facts = []
        if facts_list:
            fact_items = await facts_list.query_selector_all('li')
            facts = [(await li.inner_text()).strip() for li in fact_items]

        # Assign facts based on common patterns (this might need adjustment)
        data['price_search'] = 'N/A'
        data['units_type_search'] = 'N/A'
        data['size_search'] = 'N/A'
        if len(facts) >= 1:
            data['price_search'] = facts[0]
        if len(facts) >= 2:
            data['units_type_search'] = facts[1]
        if len(facts) >= 3:
            data['size_search'] = facts[2]

    except Exception as e:
        print(f"Error extracting data from search placard: {e}")
        # Return partial data or placeholders
        data.setdefault('title', 'Error')
        data.setdefault('link', 'Error')
        data.setdefault('address', 'Error')
        data.setdefault('price_search', 'Error')
        data.setdefault('units_type_search', 'Error')
        data.setdefault('size_search', 'Error')
    return data

async def get_property_data_from_detail_page(page):
    """Extracts detailed data from the property's detail page."""
    data = {}
    try:
        # --- PROPERTY FACTS Table ---
        # The table containing detailed facts. We'll query specific rows by data-fact-type.
        # Using the structure from Pasted_Text_1755960362240.txt and Pasted_Text_1756145388907.txt

        # --- Fact Selectors ---
        # These target the <td> containing the label, then the adjacent (+) <td> containing the value/span.
        fact_rows_selectors = {
            'price': 'td[data-fact-type="Price"] + td',
            'price_per_unit': 'td[data-fact-type="PricePerUnit"] + td',
            'property_type': 'td[data-fact-type="PropertyType"] + td',
            'property_subtype': 'td[data-fact-type="PropertySubtype"] + td',
            'no_units': 'td[data-fact-type="NoUnits"] + td',
            'year_built': 'td[data-fact-type="YearBuilt"] + td',
            'building_size': 'td[data-fact-type="BuildingSize"] + td',
            'lot_size': 'td[data-fact-type="LotSize"] + td',
            'sale_type': 'td[data-fact-type="SaleType"] + td',
            'sale_conditions': 'td[data-fact-type="SaleConditions"]', # Gets the whole cell for complex content
            'average_occupancy': 'td[data-fact-type="AverageOccupancy"] + td',
            'no_stories': 'td[data-fact-type="NoStories"] + td',
            'apartment_style': 'td[data-fact-type="ApartmentStyle"] + td',
            'cap_rate': 'td[data-fact-type="CapRate"] + td',
            'opportunity_zone': 'td.opportunity-zone[data-fact-type="OpportunityZone"] + td', # Combines class and attribute
            'building_class': 'td[data-fact-type="BuildingClass"] + td',
            'zoning': 'td[data-fact-type="Zoning"] + td', # Check if this is the correct attribute
            # Add more selectors for other fields if needed and found in the HTML
        }

        # --- Extract Fact Values ---
        for key, selector in fact_rows_selectors.items():
            try:
                # Find the cell containing the value
                value_cell = await page.query_selector(selector)
                if value_cell:
                    # Often, the value is inside a <span> within the cell
                    value_span = await value_cell.query_selector('span')
                    if value_span:
                        data[key] = (await value_span.inner_text()).strip()
                    else:
                        # If no span, get the direct text content of the cell
                        # This is important for 'sale_conditions' which might have complex HTML
                        if key == 'sale_conditions':
                             # Get full text content including potential child elements
                             data[key] = (await page.evaluate('(element) => element.textContent', value_cell)).strip()
                        else:
                             data[key] = (await value_cell.inner_text()).strip()
                else:
                    data[key] = 'N/A'
            except Exception as e:
                print(f"  Warning: Error finding detail '{key}' with selector '{selector}': {e}")
                data[key] = 'Error-Selector'

        # --- Agent Information ---
        # Placeholder - Inspect actual detail page HTML to find the correct selectors.
        # For now, indicate where to find it or mark as N/A:
        data['agent_name'] = 'N/A (Inspect detail page HTML for selector)'
        data['agent_company'] = 'N/A (Inspect detail page HTML for selector)'
        data['agent_phone'] = 'N/A (Inspect detail page HTML for selector)'
        data['agent_email'] = 'N/A (Inspect detail page HTML for selector)'

        # --- Listing ID (from URL) ---
        current_url = page.url
        # Simple extraction from URL pattern: .../Listing/.../ID/
        id_match = re.search(r'/Listing/.*?/(\d+)/', current_url)
        data['listing_id'] = id_match.group(1) if id_match else 'N/A'

    except Exception as e:
        print(f"Error extracting data from detail page: {e}")
        import traceback
        traceback.print_exc() # Print full traceback for debugging
        # Ensure keys exist even on error
        for key in fact_rows_selectors.keys():
            data.setdefault(key, 'Error-Extraction')
        data.setdefault('agent_name', 'Error-Extraction')
        data.setdefault('agent_company', 'Error-Extraction')
        data.setdefault('agent_phone', 'Error-Extraction')
        data.setdefault('agent_email', 'Error-Extraction')
        data.setdefault('listing_id', 'Error-Extraction')
    return data

async def scrape_loopnet_listings():
    """Main scraping function with enhanced strategies."""
    if not os.path.exists(CHROME_PATH):
        print(f"Chrome executable not found at {CHROME_PATH}. Please check the path.")
        return
    if not os.path.exists(USER_DATA_DIR):
        print(f"Chrome user data directory not found at {USER_DATA_DIR}. Please check the path.")
        return

    print(f"Using Chrome: {CHROME_PATH}")
    print(f"Using Profile: {USER_DATA_DIR}")
    
    # intended_profile_path = f"/home/solkiona/.config/google-chrome/Profile 2" # Or however you were setting it
    # main_config_dir = "/home/solkiona/.config/google-chrome/Profile 2"
    # profile_name = "Profile 2"

    async with async_playwright() as p:
        # --- 1. Launch your existing Chrome with your profile using launch_persistent_context ---
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR, # <<<< Pass user_data_dir directly here
            executable_path=CHROME_PATH, # <<<< Specify the Chrome executable
            headless=False, # Keep it visible for debugging and to mimic real user
            args=[
                # DO NOT include --user-data-dir in args
                # f"--user-data-dir={USER_DATA_DIR}", # <<<< REMOVE this line
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--start-maximized", # Start maximized like a user might

                # Args to reduce automation detection
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars", # Might help hide automation info bars
                # f"--profile-directory={profile_name}",
                # "--disable-extensions", # Often recommended, but removes profile extensions. Test impact.
                # "--disable-plugins", # Might be too aggressive
                # "--disable-plugins-discovery", # Might be too aggressive

                # Potentially useful, but test impact
                # "--disable-background-timer-throttling",
                # "--disable-backgrounding-occluded-windows",
                # "--disable-renderer-backgrounding",
                # "--disable-ipc-flooding-protection",
                # "--enable-features=NetworkService,NetworkServiceInProcess",
            ]
        )

        # --- 2. Configure the context further ---
        # Set extra HTTP headers on the context
        await context.set_extra_http_headers({
            # Standard headers a real browser sends.
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            # Update Sec-Ch-Ua to match your actual Chrome version (139.0.7258.138)
            "Sec-Ch-Ua": '"Chromium";v="139", "Not;A=Brand";v="24", "Google Chrome";v="139"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Linux"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            # Header observed in previous analysis
            "x-page-loopnetarea": "SRP-Client",
        })

        # --- 3. Advanced Fingerprint Spoofing (Attempt to hide Playwright) ---
        await context.add_init_script("""
            // 1. Hide the webdriver property
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });

            // 2. Make plugins look more real (basic example using Proxy)
            const originalPlugins = navigator.plugins;
            Object.defineProperty(navigator, 'plugins', {
                get: () => {
                    return new Proxy(originalPlugins, {
                        get(target, prop) {
                            if (prop === 'length') return 3;
                            if (prop === 'item') return (index) => target[index];
                            if (prop === 'namedItem') return (name) => target[name];
                            if (typeof prop === 'string' && /^\\d+$/.test(prop)) {
                                const index = parseInt(prop);
                                if (index < 3) {
                                    return {
                                        name: ['Chrome PDF Plugin', 'Chrome PDF Viewer', 'Native Client'][index],
                                        filename: ['internal-pdf-viewer', 'mhjfbmdgcfjbbpaeojofohoefgiehjai', 'internal-nacl-plugin'][index],
                                        description: ['Portable Document Format', 'Portable Document Format Viewer', 'Native Client'][index]
                                    };
                                }
                            }
                            return target[prop];
                        }
                    });
                }
            });

            // 3. Make languages look standard
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });

            // 4. Hide modifications to the chrome object if it exists
            if (window.chrome && window.chrome.runtime) {
                 delete window.chrome.runtime;
            }

        """)

        # Get the page from the context
        page = await context.new_page()

        # --- 4. Navigate to the search page with human-like delays ---
        print(f"Loading search page: {TARGET_URL}")
        # Initial delay before any action
        await asyncio.sleep(random.uniform(2, 5))
        try:
            response = await page.goto(TARGET_URL, timeout=60000, wait_until='domcontentloaded')
            print(f"Search page loaded. Status: {response.status if response else 'No Response Object'}")
            if response and response.status == 403:
                 print("Received 403 Forbidden. This might be the 'Access Denied' error.")
                 await context.close()
                 return

        except Exception as e:
             print(f"Error navigating to search page: {e}")
             await context.close()
             return

        # Longer delay after initial load to let JS render content
        await asyncio.sleep(random.uniform(5, 10))

        # --- 5. Find Listing Placards ---
        # Based on Pasted_Text_1755970997961.txt, listings are within <article> tags with placard classes.
        placard_selectors = [
            'article.placard', # Primary selector from your snippets
            'div.placard-content', # Secondary from list page snippet
            # '[data-id]', # Very generic fallback, less preferred
        ]

        listing_elements = []
        found_selector = None
        for selector in placard_selectors:
            try:
                # Wait for at least one listing to appear and be visible
                await page.wait_for_selector(selector, timeout=30000, state='visible')
                listing_elements = await page.query_selector_all(selector)
                if listing_elements:
                    found_selector = selector
                    print(f"Found listings using selector: {selector}")
                    break
            except asyncio.TimeoutError:
                print(f"Timeout waiting for listings with selector: {selector}")
                continue

        if not listing_elements:
            print("Failed to find any listing placard elements.")
            # Try to get page content for debugging
            content = await page.content()
            print(f"Page title: {await page.title()}")
            print(f"Content length: {len(content)}")
            # print(f"Content snippet: {content[:2000]}") # Uncomment for more details if needed
            await context.close()
            return

        print(f"Found {len(listing_elements)} listings. Processing first 2 for testing...")

        all_scraped_data = []
        # Process only the first 2 for initial testing to be less aggressive
        for i, listing_elem in enumerate(listing_elements[:2]): # <<< Changed to 2 for testing
            print(f"\n--- Processing Listing {i+1} ---")
            # Human-like delay between processing listings
            await asyncio.sleep(random.uniform(2, 4))

            # 1. Get data from search results page
            search_data = await get_property_data_from_search_page(listing_elem)
            print(f"  Search Data Extracted: {list(search_data.keys())}")

            listing_url = search_data.get('link')
            if not listing_url or listing_url in ['N/A', 'Error']:
                print("  Skipping: No valid link found.")
                all_scraped_data.append({**search_data, 'status': 'Skipped - No Link'})
                continue

            # 2. Navigate to the detail page with delays
            print(f"  Navigating to detail page: {listing_url}")
            await asyncio.sleep(random.uniform(3, 6)) # Longer delay before navigation
            try:
                detail_response = await page.goto(listing_url, timeout=60000, wait_until='domcontentloaded')
                print(f"  Detail page status: {detail_response.status if detail_response else 'No Response Object'}")
                if detail_response and detail_response.status == 403:
                     print("  Received 403 on detail page.")
                     all_scraped_data.append({**search_data, 'status': 'Error - 403 on Detail Page'})
                     await page.go_back()
                     await asyncio.sleep(2)
                     continue

                # Wait for key elements on the detail page to load (PROPERTY FACTS table is crucial)
                await page.wait_for_selector('table, .property-facts, h1', timeout=30000, state='visible')
                await asyncio.sleep(random.uniform(2, 4)) # Extra delay after page load stabilizes
            except Exception as e:
                print(f"  Error navigating to detail page: {e}")
                all_scraped_data.append({**search_data, 'status': f'Error - Navigation: {e}'})
                await page.go_back()
                await asyncio.sleep(2)
                continue

            # 3. Get data from detail page
            detail_data = await get_property_data_from_detail_page(page)
            print(f"  Detail Data Extracted Keys: {list(detail_data.keys())}")

            # 4. Combine data
            combined_data = {**search_data, **detail_data, 'status': 'Success'}
            all_scraped_data.append(combined_data)

            # 5. Go back to search results
            print("  Returning to search results...")
            await page.go_back()
            # Delay after going back
            await asyncio.sleep(random.uniform(3, 5))

        # --- Print Final Results ---
        print("\n" + "="*50)
        print("FINAL SCRAPED DATA (First 2 Listings - Testing)")
        print("="*50)
        for i, property_data in enumerate(all_scraped_data):
            print(f"\n--- Property {i+1} ---")
            # Print in a more readable format, potentially mapping to task fields
            print(f"  Status: {property_data.get('status', 'N/A')}")
            print(f"  Title: {property_data.get('title', 'N/A')}")
            print(f"  Link: {property_data.get('link', 'N/A')}")
            print(f"  Address (Search): {property_data.get('address', 'N/A')}")
            print(f"  Asking Price: {property_data.get('price', property_data.get('price_search', 'N/A'))}")
            print(f"  Property Type: {property_data.get('property_type', 'N/A')} ({property_data.get('property_subtype', 'N/A')})")
            print(f"  Number of Units: {property_data.get('no_units', 'N/A')}")
            print(f"  Year Built: {property_data.get('year_built', 'N/A')}")
            print(f"  Building Size: {property_data.get('building_size', 'N/A')}")
            print(f"  Lot Size: {property_data.get('lot_size', 'N/A')}")
            print(f"  Cap Rate: {property_data.get('cap_rate', 'N/A')}")
            print(f"  Sale Conditions: {property_data.get('sale_conditions', 'N/A')}")
            print(f"  Agent Name: {property_data.get('agent_name', 'N/A')}")
            print(f"  Agent Company: {property_data.get('agent_company', 'N/A')}")
            print(f"  Agent Phone: {property_data.get('agent_phone', 'N/A')}")
            print(f"  Agent Email: {property_data.get('agent_email', 'N/A')}")
            print(f"  Listing ID: {property_data.get('listing_id', 'N/A')}")
            # Add more fields as needed for debugging

        # await context.close() # Use context.close() instead of browser.close()
        print("\nScraping session finished.")


# Run the scraper
if __name__ == '__main__':
    asyncio.run(scrape_loopnet_listings())