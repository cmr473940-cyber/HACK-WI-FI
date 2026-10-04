from time import sleep
from playwright.sync_api import sync_playwright

with open('random.txt', 'r', encoding='utf-8') as f:

    with sync_playwright() as p :

        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("http://www.g.net/index.html")

        for line in f :
            page.fill(".login-input" , line.strip())
            page.click(".login-submit")
            page.click(".error-container")

            sleep(1.5)
