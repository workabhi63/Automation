import re
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com/ncr", wait_until="domcontentloaded")

    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No poup found, continuing.....")
    
    # page.get_by_role("combobox",name="Search").wait_for(state="visible",timeout=60000)
    page.get_by_role("combobox",name="Search").fill("Playwright")
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))

    