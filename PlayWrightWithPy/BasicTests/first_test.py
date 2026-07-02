from playwright.sync_api import sync_playwright

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Open a new browser page/tab
        page = browser.new_page()
        
        # Navigate to the target website
        page.goto("https://www.google.com")
        
        # Retrieve and print the page title
        print(f"Page Title: {page.title()}")
        
        # Close the browser session
        browser.close()