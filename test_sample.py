from playwright.sync_api import sync_playwright
def test_example(): # this is a simple test function that checks if 1 + 1 equals 2
    assert 1 + 1 == 2
    
def test_title(): # opens a webpage and checks if title is correct
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="msedge")
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        assert page.title() == "Automation Testing Practice"
        browser.close()