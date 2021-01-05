class Manacher:
    def __init__(self, s):
        self.s = s
        self.t = ["#"]  # "#" must not include in s
        for char in s:
            self.t.append(char)
            self.t.append("#")
        self.n = len(self.t)
        self.len_p = [0] * self.n
        self.build()

    def build(self):
        i, j = 0, 0
        while i < self.n:
            while i - j >= 0 and i + j < self.n and self.t[i - j] == self.t[i + j]:
                j += 1
            self.len_p[i] = j
            k = 1
            while i - k >= 0 and i + k < self.n and k + self.len_p[i - k] < j:
                self.len_p[i + k] = self.len_p[i - k]
                k += 1
            i += k
            j -= k
        self.len_p = [val - 1 for val in self.len_p]

    def longest(self):
        max_len, center_idx = max((l, i) for i, l in enumerate(self.len_p))
        return self.s[(center_idx - max_len) // 2: (center_idx + max_len) // 2]
