class Node:
    def __init__(self, back=None, url=None, forward=None):
        self.back = back
        self.url = url
        self.forward = forward


class BrowserHistory:
    def __init__(self, url=None):
        self._head = Node(url=url)
        self._curr = self._head

    def visit(self, url):
        prev, page = self._curr, Node(url=url)
        prev.forward = page
        page.back = prev
        self._curr = page

    def back(self, steps):
        ptr = self._curr
        while ptr.back and steps > 0:
            ptr = ptr.back
            steps -= 1
        self._curr = ptr
        return self._curr.url

    def forward(self, steps):
        ptr = self._curr
        while ptr.forward and steps > 0:
            ptr = ptr.forward
            steps -= 1
        self._curr = ptr
        return self._curr.url

    def __iter__(self):
        ptr = self._head
        while ptr:
            yield ptr.url
            ptr = ptr.forward
