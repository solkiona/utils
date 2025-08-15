import requests
import time
import random
from urllib.parse import urlparse

def advanced_request(url, use_proxy=True):
    """
    Advanced request with multiple evasion techniques
    """
    
    # Working proxies from your test
    proxies_list = [
        "209.135.168.41:80",      # US
        "103.130.145.197:80",     # Turkey  
        "103.105.76.209:8080",    # Indonesia
        "91.99.78.151:80"         # Germany
    ]
    
    # Realistic User Agents (recent browsers)
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0'
    ]
    
    # Parse URL for referer
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    
    # Create realistic headers
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # Add referer to look like you came from their homepage
        'Referer': base_url
    }
    
    # Create session for cookie persistence
    session = requests.Session()
    session.headers.update(headers)
    
    # Try with proxies first
    if use_proxy:
        for proxy in proxies_list:
            try:
                proxies = {
                    'http': f'http://{proxy}',
                    'https': f'http://{proxy}'
                }
                
                print(f"Trying proxy: {proxy}")
                
                # Add random delay to mimic human behavior
                time.sleep(random.uniform(2, 5))
                
                # Make request
                response = session.get(
                    url, 
                    proxies=proxies, 
                    timeout=20,
                    allow_redirects=True
                )
                
                print(f"Status: {response.status_code}")
                
                if response.status_code == 200:
                    print(f"✅ Success with proxy {proxy}")
                    return response
                elif response.status_code == 403:
                    print(f"❌ 403 Forbidden with proxy {proxy}")
                elif response.status_code == 429:
                    print(f"⚠️ Rate limited with proxy {proxy}")
                else:
                    print(f"⚠️ Unexpected status {response.status_code} with proxy {proxy}")
                    
            except Exception as e:
                print(f"❌ Proxy {proxy} failed: {str(e)[:80]}")
                continue
    
    # Try without proxy as fallback
    try:
        print("Trying without proxy...")
        time.sleep(random.uniform(3, 6))
        
        response = session.get(
            url, 
            timeout=15,
            allow_redirects=True
        )
        
        print(f"Direct request status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Success without proxy")
            return response
        else:
            print(f"❌ Direct request failed with status {response.status_code}")
            
    except Exception as e:
        print(f"❌ Direct request failed: {e}")
    
    return None

def try_homepage_first(target_url):
    """
    Visit homepage first to establish session, then target page
    """
    parsed_url = urlparse(target_url)
    homepage = f"{parsed_url.scheme}://{parsed_url.netloc}"
    
    print(f"Step 1: Visiting homepage {homepage}")
    
    # Visit homepage first
    homepage_response = advanced_request(homepage, use_proxy=True)
    
    if homepage_response and homepage_response.status_code == 200:
        print("✅ Homepage visit successful")
        time.sleep(random.uniform(3, 7))  # Human-like pause
        
        print(f"Step 2: Visiting target page")
        return advanced_request(target_url, use_proxy=True)
    else:
        print("❌ Homepage visit failed, trying target directly")
        return advanced_request(target_url, use_proxy=True)

# Test the function
if __name__ == "__main__":
    url = "https://www.naijanews.com/2025/06/19/benue-how-could-anyone-think-it-appropriate-to-stage-a-spectacle-while-hundreds-of-citizens-lie-dead-nnpp-blasts-tinubu-alia/"
    
    print("=== Advanced Scraping Attempt ===")
    response = try_homepage_first(url)
    
    if response:
        print(f"\n✅ SUCCESS! Status: {response.status_code}")
        print(f"Content length: {len(response.text)}")
        print(f"First 200 chars: {response.text[:200]}")
    else:
        print("\n❌ All methods failed")