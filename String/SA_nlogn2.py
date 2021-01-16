class SuffixArray:
    def __init__(self, string):
        self.n = len(string)
        self.sa = [i for i in range(self.n + 1)]
        self.lcp = [0] * (self.n + 1)
        if type(string[0]) == str:
            array = [ord(char) for char in string]
        else:
            array = string
        self.build_SA(array)
        self.build_LCP(array)

    def build_SA(self, array):
        rank = [-1] * (2 * self.n + 1)
        rank[0:self.n] = array

        tmp = [0] * (self.n + 1)
        cmp_sa = lambda i: (rank[i] << 32) | (rank[i + k] + 1)

        k = 1
        while k <= self.n:
            self.sa.sort(key=cmp_sa)
            val = self.sa[0]
            tmp[val] = 0
            for nxt_val in self.sa[1:]:
                tmp[nxt_val] = tmp[val] + (cmp_sa(val) < cmp_sa(nxt_val))
                val = nxt_val
            rank[0:self.n + 1] = tmp
            k <<= 1

    def build_LCP(self, array):
        rank = [0] * (self.n + 1)
        for i, val in enumerate(self.sa):
            rank[val] = i
        h = 0
        for i, rk in enumerate(rank):
            j = self.sa[rk - 1]
            if h > 0:
                h -= 1
            while j + h < self.n and i + h < self.n:
                if array[j + h] != array[i + h]:
                    break
                else:
                    h += 1
            self.lcp[rk - 1] = h
