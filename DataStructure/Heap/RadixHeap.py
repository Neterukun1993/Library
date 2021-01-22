class RadixHeap:
    def __init__(self, LIMIT):
        self.LIMIT = LIMIT
        self.vals = [[] for i in range(LIMIT.bit_length() + 1)]
        self.size = 0
        self.last = 0

    def __len__(self):
        return self.size

    def push(self, key, val):
        if key > self.LIMIT:
            raise RuntimeError(f'A pushed value {x} must be no more than {self.LIMIT}')
        if self.last > key:
            raise RuntimeError(f'A pushed value {x} must be not less than the last poped value')
        self.size += 1
        self.vals[(key ^ self.last).bit_length()].append((key, val))

    def pop(self):
        if self.size == 0:
            raise IndexError('pop from empty heapq')
        if not self.vals[0]:
            i = 1
            while not self.vals[i]:
                i += 1
            self.last = min([key for key, _ in self.vals[i]])
            for key, val in self.vals[i]:
                self.vals[(key ^ self.last).bit_length()].append((key, val))
            self.vals[i] = []
        self.size -= 1
        return self.vals[0].pop()
