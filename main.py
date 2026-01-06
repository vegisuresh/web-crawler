from config import DOMAIN_DELAY, MAX_PAGES
from crawler import crawl
from scheduler import Scheduler
from storage import save


def main():
    scheduler = Scheduler()
    scheduler.add("https://eficens.ai", priority=0)

    crawled_count = 0

    while crawled_count < MAX_PAGES:
        url = scheduler.next()
        if not url:
            break

        links = crawl(url, DOMAIN_DELAY)
        save(url)
        crawled_count += 1

        print(f"\nCrawled [{crawled_count}]: {url}")
        print(f"Discovered {len(links)} links")

        for link in links:
            scheduler.add(link, priority=crawled_count + 1)


if __name__ == "__main__":
    main()
