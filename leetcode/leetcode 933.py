# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        smallest = max(t - 3000, 0)
        while self.requests[0] < smallest:
            self.requests.pop(0)
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)