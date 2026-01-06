import hashlib

seen_urls = set()
seen_content = set()
scheduled_urls = set()


def is_url_seen(url):
    if url in seen_urls:
        return True
    seen_urls.add(url)
    return False


def is_url_scheduled(url):
    if url in scheduled_urls:
        return True
    scheduled_urls.add(url)
    return False


def is_content_seen(content):
    h = hashlib.sha256(content.encode("utf-8")).hexdigest()
    if h in seen_content:
        return True
    seen_content.add(h)
    return False
