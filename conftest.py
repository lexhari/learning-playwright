# file serves as configuration to define fixtures that
# can be used across multiple test files
# allows for reusable setup
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function") # defines a fixture with a scope of "function",
# meaning it will be executed for each test function that uses it
def browser(): #fixture function that sets up and tears down the browser for each test
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # launches a Chromium browser instance in non-headless mode
        yield browser  # yields the browser instance to the test function
        browser.close()  # ensures that the browser is closed after the test is completed

@pytest.fixture # defines another fixture ; no scope specified, so it defaults to "function"
def page(browser): # takes the browser fixture as an argument, allowing it to use the browser instance created by the browser fixture
    page = browser.new_page()  # creates a new page (tab) in the browser
    yield page  # yields the page to the test function
    page.close()  # ensures that the page is closed after the test is completed
    
# in a test, it can be used as:
# def test_example(page):
#     page.goto("https://example.com")