from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as scrapper:
    browser = scrapper.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.linkedin.com/home')
    page.fill('input#session_key','jeremyloki93@gmail.com')
    page.fill('input#session_password', 'XaKYF?K+Mxn3q2H')
    page.click('button[type=submit]')
    page.goto('https://www.linkedin.com/jobs/')
    # page.fill('input#jobs-search-box-keyword-id-ember198','react js')
    # page.fill('input#jobs-search-box-location-id-ember22', 'Remote')
    # page.click('button[type=button]')
    html = page.content('scaffold-layout__list-container')
    print(html);

