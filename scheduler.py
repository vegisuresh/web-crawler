import heapq


class Scheduler:

    def __init__(self):
        self.queue = []

    def add(self, url, priority):
        """Add a URL to the scheduler with a given priority."""
        heapq.heappush(self.queue, (priority, url))

    def next(self):
        if not self.queue:
            return None
        return heapq.heappop(self.queue)[1]
