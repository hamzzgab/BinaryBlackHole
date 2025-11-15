class DynamicArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [-1] * self.capacity
        self.len = 0

    def get(self, i):
        if i < self.capacity:
            return self.arr[i]
        return None

    def set(self, i, n):
        if i < self.capacity:
            self.arr[i] = n

    def pushback(self, n):
        if self.is_full():
            self.resize()
        self.arr[self.len] = n
        self.len += 1

    def pop(self):
        if not self.is_empty():
            val = self.arr[self.len - 1]
            self.arr[self.len - 1] = -1
            self.len -= 1
            return val
        return None

    def get_size(self) -> int:
        return self.len

    def resize(self):
        self.capacity *= 2
        self.arr += [-1] * (self.capacity // 2)

    def is_full(self):
        return self.len == self.capacity

    def is_empty(self):
        return self.len == 0

    def get_capacity(self) -> int:
        return self.capacity
