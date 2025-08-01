from src.main.linked_list.doubly.leet.design_browser_history import BrowserHistory


class TestBrowserHistory:
    def setup_method(self):
        self.dll = None

    def test_default_url_history_is_created(self):
        self.dll = BrowserHistory("test-url")
        assert list(self.dll) == ["test-url"]

    def test_visit_url(self):
        self.dll = BrowserHistory("first-page")
        self.dll.visit("second-page")
        self.dll.visit("third-page")
        assert list(self.dll) == ["first-page", "second-page", "third-page"]

    def test_history_can_go_back(self):
        self.dll = BrowserHistory("first-page")
        self.dll.visit("second-page")

        assert self.dll.back(0) == "second-page"
        assert self.dll.back(1) == "first-page"
        assert self.dll.back(2) == "first-page"

    def test_history_can_go_forward(self):
        self.dll = BrowserHistory("first-page")
        self.dll.visit("second-page")
        self.dll.visit("third-page")
        self.dll.back(2)

        assert self.dll.forward(0) == "first-page"
        assert self.dll.forward(1) == "second-page"
        assert self.dll.forward(2) == "third-page"
        assert self.dll.forward(3) == "third-page"

    def test_visit_url_clears_forward_history(self):
        self.dll = BrowserHistory("first-page")
        self.dll.visit("second-page")
        self.dll.back(1)
        self.dll.visit("third-page")

        assert list(self.dll) == ["first-page", "third-page"]
