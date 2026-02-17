# This first test opens a webpage and returns the title of the page
# Opens Microsoft Edge browser

from playwright.sync_api import (
    sync_playwright,
)  # this library provides the necessary functions to interact with browsers

with sync_playwright() as p:  # sync_playwright is the entry point ; as p is an instance of Playwright for us to use browser
    browser = p.chromium.launch(
        headless=False, channel="msedge"
    )  # stores a Chromium browser instance in the variable browser ;
    # p.chromium.launch() launches a new browser instance ;
    # headless=False makes the browser visible ; headless=True would run it in the background (faster but cant see)
    # channel="msedge" specifies to use Microsoft Edge browser
    page = browser.new_page()  # stores a new browser tab in the variable page
    page.goto(
        "https://testautomationpractice.blogspot.com/"
    )  # goto() navigates to the specified URL
    print(page.title())  # prints the title of the page
    # Keep the browser open for a while to see the result
    page.wait_for_timeout(
        5000
    )  # wait_for_timeout() pauses execution for the specified time in milliseconds
    browser.close()  # closes the browser instance
