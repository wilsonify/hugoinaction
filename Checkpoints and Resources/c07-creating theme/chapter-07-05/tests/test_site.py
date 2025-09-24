"""

Pages load successfully (return status 200).

Critical links work (navigation between pages).

Assets load (CSS, JS, images aren’t broken).

SEO/metadata basics (robots.txt, sitemap.xml, favicon).

Error page exists (404.html renders).

"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

base_url = "http://localhost:1313"


def fetch_status(browser, url):
    return browser.execute_async_script("""
        const url = arguments[0];
        const callback = arguments[1];
        fetch(url)
          .then(r => callback(r.status))
          .catch(() => callback(0));
    """, url)


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--headless=new")  # run headless for CI
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


core_pages = [
    "/", "/about/", "/contact/", "/credits/",
    "/privacy/", "/terms/", "/categories/", "/tags/"
]


@pytest.mark.parametrize("path", core_pages)
def test_core_pages_load(browser, path):
    browser.get(f"{base_url}{path}")
    assert "404" not in browser.title.lower(), f"{path} rendered a 404"
    assert browser.title != "", f"{path} has empty <title>"


def test_css_and_js_assets(browser):
    browser.get(base_url)
    links = [el.get_attribute("href") for el in browser.find_elements(By.TAG_NAME, "link")]
    scripts = [el.get_attribute("src") for el in browser.find_elements(By.TAG_NAME, "script")]
    assets = [u for u in links + scripts if u]

    for url in assets:
        status = fetch_status(browser, url)
        assert status == 200, f"Broken asset: {url}"


def test_images_not_broken(browser):
    browser.get(base_url)
    imgs = [el.get_attribute("src") for el in browser.find_elements(By.TAG_NAME, "img")]
    for src in imgs:
        status = fetch_status(browser, src)
        assert status == 200, f"Broken image: {src}"


def test_seo_basics(browser):
    for path in ["/robots.txt", "/sitemap.xml", "/favicon.ico"]:
        browser.get(f"{base_url}{path}")
        assert "404" not in browser.title.lower(), f"{path} missing"


def test_custom_404(browser):
    browser.get(f"{base_url}/non-existent-page")
    body_text = browser.find_element(By.TAG_NAME, "body").text.lower()
    assert "404" in body_text or "not found" in body_text, "Custom 404 page missing"
