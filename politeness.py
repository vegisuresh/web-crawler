import time
from urllib.parse import urlparse

last_access = {}


def wait_if_needed(url, delay):
    domain = urlparse(url).netloc
    now = time.time()

    if domain in last_access:
        elapsed = now - last_access[domain]
        if elapsed < delay:
            time.sleep(delay - elapsed)

    last_access[domain] = time.time()
