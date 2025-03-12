class DynamicArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [-1] * self.capacity
        self.len = 0

    def get(self, i):
        if i < self.capacity:
            return self.arr[i]

    def set(self, i, n):
        if i < self.capacity:
            self.arr[i] = n

    def pushback(self, n):
        if self.len == self.capacity:
            self.resize()
        self.arr[self.len] = n
        self.len += 1

    def pop(self):
        if self.len > 0:
            val = self.arr[self.len - 1]
            self.arr[self.len - 1] = -1
            self.len -= 1
            return val

    def get_size(self) -> int:
        return self.len

    def resize(self):
        self.capacity *= 2
        self.arr += [-1] * (self.capacity // 2)

    def get_capacity(self) -> int:
        return self.capacity
