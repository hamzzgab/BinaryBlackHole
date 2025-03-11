from typing import Optional, List


class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.arr: List[int] = [-1] * self.capacity
        self.len: int = 0

    def get(self, i: int) -> Optional[int]:
        if i < self.capacity:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.capacity:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()
        self.arr[self.len] = n
        self.len += 1

    def popback(self) -> Optional[int]:
        if self.len > 0:
            val = self.arr[self.len - 1]
            self.arr[self.len - 1] = -1
            self.len -= 1
            return val

    def resize(self) -> None:
        self.capacity *= 2
        self.arr += [-1] * (self.capacity // 2)

    def get_size(self) -> int:
        return self.len

    def get_capacity(self) -> int:
        return self.capacity
