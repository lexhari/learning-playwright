import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None: # copy pasted from codegen recording
    page.goto("https://testautomationpractice.blogspot.com/")
    expect(page.get_by_role("heading", name="Automation Testing Practice")).to_be_visible()
    expect(page.locator("h1")).to_contain_text("Automation Testing Practice")
    expect(page.get_by_label("Country:")).to_have_value("usa");
