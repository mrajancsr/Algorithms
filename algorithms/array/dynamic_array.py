"""Implementation of Dynamic Array using ctypes"""

import ctypes  # provides support for low level arrays
from dataclasses import dataclass, field


@dataclass
class DynamicArray:
    n: int = field(init=False, default=0)
    capacity: int = field(init=False, default=1)
    A: ctypes.py_object = field(init=False)

    def __post_init__(self):
        self.A = self._make_array(self.capacity)

    def __repr__(self):
        return f"DynamicArray({[self.A[i] for i in range(self.n)]})"

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError("Array Index Out of Bounds")
        return self.A[k]

    def __setitem__(self, k, val):
        if not 0 <= k < self.n:
            raise IndexError("Array Index Out of Bounds")
        self.A[k] = val

    def append(self, val):
        if self.capacity == self.n:
            self._resize(2 * self.capacity)
        self.A[self.n] = val
        self.n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


if __name__ == "__main__":
    # used only for testing code
    dyn_array = DynamicArray()
    dyn_array.append(4)
    dyn_array.append(10)
    dyn_array.append(15)

    print(dyn_array)
