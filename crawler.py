import requests
from config import USER_AGENT
from dedupe import is_content_seen, is_url_seen
from extract import extract_links, extract_links_js
from politeness import wait_if_needed


def crawl(url, delay):
    if is_url_seen(url):
        return set()

    wait_if_needed(url, delay)

    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=15)

        if response.status_code != 200:
            return set()

        html = response.text

        if is_content_seen(html):
            return set()

        links = extract_links(html, url)

        # 🔥 JS fallback
        if not links:
            links = extract_links_js(url)

        return links

    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return set()
