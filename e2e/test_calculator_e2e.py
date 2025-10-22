# e2e/test_calculator_e2e.py

from playwright.sync_api import sync_playwright

def test_homepage_shows_welcome_message():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/")
        body = page.inner_text("body")
        assert "Welcome to the FastAPI Calculator" in body
        browser.close()
