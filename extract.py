from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

SKIP_PREFIXES = ("mailto:", "tel:", "javascript:", "#")

BLOCKED_DOMAINS = {"twitter.com", "linkedin.com", "facebook.com"}


def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()

        # ✅ FIX HERE
        if any(href.startswith(prefix) for prefix in SKIP_PREFIXES):
            continue

        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)
        # 🚫 Block social domains
        if parsed.netloc in BLOCKED_DOMAINS:
            continue

        if parsed.scheme in ("http", "https"):
            links.add(absolute)

    return links


def extract_links_js(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=20000)
        page.wait_for_load_state("networkidle")

        links = set(
            page.eval_on_selector_all(
                "a[href]", "elements => elements.map(e => e.href)"
            )
        )

        browser.close()
        return links
