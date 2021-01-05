class SuffixArray:
    def __init__(self, string):
        self.n = len(string)
        self.sa = [0] * (self.n + 1)
        self.lcp = [0] * (self.n + 1)
        if type(string[0]) == str:
            array = [ord(char) for char in string]
        else:
            array = string
        array = self.compress(array)
        self.build_SA(array)
        self.build_LCP(array)

    def compress(self, array):
        memo = {val: idx for idx, val in enumerate(sorted(set(array)))}
        array = [memo[val] + 1 for val in array]
        return array

    def build_SA(self, array):
        array = array + [0]
        n = len(array)
        c = [0] * n
        cnt = [0] * n
        cn = [0] * n

        for val in array:
            cnt[val] += 1
        for i in range(1, n):
            cnt[i] += cnt[i - 1]
        for i, val in enumerate(array):
            cnt[val] -= 1
            self.sa[cnt[val]] = i

        c[self.sa[0]] = 0
        classes = 1
        for i in range(1, n):
            if array[self.sa[i]] != array[self.sa[i - 1]]:
                classes += 1
            c[self.sa[i]] = classes - 1

        k = 0
        while (1 << k) < n:
            shift = 1 << k
            pn = [(self.sa[i] - shift) % n for i in range(n)]

            for i in range(classes):
                cnt[i] = 0
            for i in pn:
                cnt[c[i]] += 1
            for i in range(1, classes):
                cnt[i] += cnt[i - 1]
            for i in reversed(pn):
                cnt[c[i]] -= 1
                self.sa[cnt[c[i]]] = i

            prv_idx = self.sa[0]
            cn[prv_idx] = 0
            classes = 1
            for cur_idx in self.sa[1:]:
                cur = c[cur_idx], c[(cur_idx + shift) % n]
                prv = c[prv_idx], c[(prv_idx + shift) % n]
                if cur != prv:
                    classes += 1
                cn[cur_idx] = classes - 1
                prv_idx = cur_idx
            c, cn = cn, c
            k += 1

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
