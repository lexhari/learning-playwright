# Playwright
I tried to learn Selenium but I decided to learn Playwright first.

## What is Playwright
- Open source framework for web automation testing created by Microsoft
- Supports Web browser apps, mobile web apps and API
- JavaScript, TypeScript, Java, Python, .NET (C#)
- Supports Chromium, WebKit, and Firefox
- Supports Windows, MachOS, Linux and CI runs

[Playwright](https://www.playwright.dev)
[Playwright Github](https://www.github.com/microsoft/playwright)

## Features of Playwright
- Free and Open Source
- Multi-browser, multi-language, multi-OS
- Easy setup and configuration
- Functional, API, accessibility testing
- Built-in reporters, custom reporters
- CI/CD, Docker support
- Records tests, debugs tests, and explore selectors
- Parallel testing: run playwright on multiple browsers at the same time
- Auto wait
- Built in assertions meaning less flaky tests (sometimes it passes then sometimes it fails)
- Test retry, logs, screenshots, videos
- Multi-tab and multi-window executions
- Frames, Shadow DOM
- Emulate mobile devices , geolocations
- Test parameterization: use other files
- Fast

# Playwright vs Playwright with Pytest
* `pip install playwright`: installs core playwright API
* `pip install pytest-playwright`: adds pytest integrations (fixtures, CLI support) ; testing framework for Python for simple scalable and readable test cases ; suitable for testing projects/frameworks, giving us alot of options

These two are compatible and often used together. Playwright gives the raw API, pytest gives test structure and automation convenience.

## Writing a PyTest
### What is a test in PyTest?
- A test is a function whose name starts with `test_`
- Pytest automatically finds and runs these