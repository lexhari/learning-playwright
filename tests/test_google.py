import re 
# regex module: used for working with regular expressions,
# which are patterns used to match character combinations in strings.
# In testing, regex can be used to validate input formats,
# extract specific information from strings, or perform complex string manipulations.

from playwright.sync_api import expect
# expect function: used for making assertions in tests,
# allowing you to verify that certain conditions are met
# (e.g., checking if an element is visible, contains specific text, etc.)

def test_google_search(page): # page is a fixture that automatically provides a new browser page for each test
    # page fixture doesn't require manual setup or teardown of the browser page
    
    page.wait_for_timeout(3000)  # wait for 2 seconds to ensure the page is fully loaded before interacting with it
    
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)  # clicks the "Accept all" button
    except:
        pass  # if the button is not found, it will simply ignore the error and continue with the test
    
    # get_by_role() is a method that finds elements based on their ARIA role and name, 
    # which is useful for accessibility testing
    
    # generally, get_by requires the tester to review the page's HTML via
    # browser developer tools to identify the correct role and name for the element they want to interact with.
    
    page.get_by_role("combobox", name="Search").fill("Playwright")  # fills the search box with "Playwright"
    # combobox role: typically used for input fields that
    # allow users to select from a list of options or enter their own value
    # name="Search" helps to identify the specific search box element on the page
    
    page.keyboard.press("Enter")  # simulates pressing the Enter key to submit the search
    
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))  # asserts that the page title contains "Playwright"
    # to_have_title() is an assertion method that checks if the page title matches the specified
    # regular expression (regex) pattern, which allows for flexible matching of the title content.
    # re.compile is used to create a regex pattern that can be used for matching the title,
    # allowing for variations in the title while still ensuring it contains the keyword "Playwright".
    # re.IGNORECASE makes the regex case-insensitive, so it will match "Playwright", "playwright", "PLAYWRIGHT", etc.
    