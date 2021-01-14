class DAryHeap:
    def __init__(self, D=2):
        self.heap = []
        self.D = D

    def __len__(self):
        return len(self.heap)

    @property
    def min(self):
        return self.heap[0]

    def push(self, val):
        self.heap.append(val)
        idx = len(self) - 1
        par = (idx - 1) // self.D
        while par >= 0 and self.heap[idx] < self.heap[par]:
            self.heap[idx], self.heap[par] = self.heap[par], self.heap[idx]
            idx, par = par, (par - 1) // self.D

    def pop(self):
        if not self:
            raise IndexError('pop from empty heap')
        if len(self) == 1:
            return self.heap.pop()
        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        idx = 0
        while True:
            min_val = self.heap[idx]
            chi = -1
            for i in range(1, self.D + 1):
                tmp_chi = idx * self.D + i
                if tmp_chi < len(self) and min_val > self.heap[tmp_chi]:
                    min_val = self.heap[tmp_chi]
                    chi = tmp_chi
            if chi == -1:
                break
            if self.heap[idx] > self.heap[chi]:
                self.heap[idx], self.heap[chi] = self.heap[chi], self.heap[idx]
            idx = chi
        return res
