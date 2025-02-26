import unittest


class BrowserHistory:
    urls: list[str] = []
    cur: int = 0

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        while len(self.urls) > self.cur + 1:
            self.urls.pop()
        self.urls.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur = max(self.cur - steps, 0)
        return self.urls[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps, len(self.urls) - 1)
        return self.urls[self.cur]


class TestBrowserHistory(unittest.TestCase):
    def test(self):
        browser_history = BrowserHistory("leetcode.com")
        browser_history.visit("google.com")
        browser_history.visit("facebook.com")
        browser_history.visit("youtube.com")
        url = browser_history.back(1)
        self.assertEqual("facebook.com", url)
        url = browser_history.back(1)
        self.assertEqual("google.com", url)
        url = browser_history.forward(1)
        self.assertEqual("facebook.com", url)

        browser_history.visit("linkedin.com")
        url = browser_history.forward(2)
        self.assertEqual("linkedin.com", url)

        url = browser_history.back(2)
        self.assertEqual("google.com", url)


if __name__ == '__main__':
    unittest.main()
