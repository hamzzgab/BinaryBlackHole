import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Stack:
    def __init__(self, _empty_val=-1, _max=5):
        self._max = _max
        self._top = -1
        self._empty_val = _empty_val
        self.stack = [self._empty_val] * self._max

    def push(self, val):
        if not self.is_full():
            self._top += 1
            self.stack[self._top] = val
            logging.log(logging.INFO,
                        f"Pushed value: {val}, top: {self._top}, max: {self._max}, stack: {self}")
        else:
            logging.log(logging.WARN,
                        f"Array is full, resize?, top: {self._top}, max: {self._max}, stack: {self}")
            return None

    def pop(self):
        if not self.is_empty():
            popped_val = self.stack[self._top]
            self.stack[self._top] = self._empty_val
            self._top -= 1
            logging.log(logging.INFO,
                        f"Popped value: {popped_val}, top: {self._top}, max: {self._max}, stack: {self}")
            return popped_val
        else:
            logging.log(logging.WARN,
                        f"Array is empty, add elements?, top: {self._top}, max: {self._max}, stack: {self}")
            return -1

    def top(self):
        if not self.is_empty():
            return self.stack[self._top]
        else:
            logging.log(logging.WARN,
                        f"Array is empty, add elements?, top: {self._top}, max: {self._max}, stack: {self}")
            return -1

    def __str__(self):
        return " > ".join(str(val) for val in self.stack[self._top::-1]) if not self.is_empty() else ""

    def __len__(self):
        return self._top + 1

    def is_full(self):
        return True if self._top == (self._max - 1) else False

    def is_empty(self):
        return True if self._top == -1 else False
