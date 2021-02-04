class ArrayDeque:
    def __init__(self):
        self.arr_size = 1
        self.array = [0]
        self.n = 0
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.n

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i >= self.n:
            raise StopIteration
        self._i += 1
        return self.array[(self.head + self._i - 1) & (self.arr_size - 1)]

    def __getitem__(self, i):
        if i < 0:
            i = self.n + i
        if not (0 <= i < self.n):
            raise IndexError
        return self.array[(self.head + i) & (self.arr_size - 1)]

    def __setitem__(self, i, val):
        if i < 0:
            i = self.n + i
        if not (0 <= i < self.n):
            raise IndexError
        self.array[(self.head + i) & (self.arr_size - 1)] = val

    def _resize(self):
        new_arr = [0] * ((self.n + 1) << 1)
        for i in range(self.n):
            new_arr[i] = self.array[(self.head + i) & (self.arr_size - 1)]
        self.array = new_arr
        self.arr_size = (self.n + 1) << 1
        self.head = 0
        self.tail = self.n

    def append(self, val):
        if self.n == self.arr_size - 1:
            self._resize()
        self.array[self.tail] = val
        self.tail = (self.tail + 1) & (self.arr_size - 1)
        self.n += 1

    def appendleft(self, val):
        if self.n == self.arr_size - 1:
            self._resize()
        self.head = (self.head - 1) & (self.arr_size - 1)
        self.array[self.head] = val
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise IndexError
        self.tail = (self.tail - 1) & (self.arr_size - 1)
        val = self.array[self.tail]
        self.n -= 1
        if self.arr_size >= 4 * self.n + 2:
            self._resize()
        return val

    def popleft(self):
        if self.n == 0:
            raise IndexError
        val = self.array[self.head]
        self.head = (self.head + 1) & (self.arr_size - 1)
        self.n -= 1
        if self.arr_size >= 4 * self.n + 2:
            self._resize()
        return val

    def clear(self):
        self.__init__()
