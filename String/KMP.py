class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        self.next = [0] * (len(pattern) + 1)
        self.next[0] = -1
        j = -1
        for i in range(len(pattern)):
            while j >= 0 and pattern[i] != pattern[j]:
                j = self.next[j]
            j += 1
            if i + 1 < len(pattern) and pattern[i + 1] == pattern[j]:
                self.next[i + 1] = self.next[j]
            else:
                self.next[i + 1] = j

    def match(self, text):
        idxs = []
        i, j = 0, 0
        while i + j < len(text):
            if self.pattern[j] == text[i + j]:
                j += 1
                if j != len(self.pattern):
                    continue
                idxs.append(i)
            i += j - self.next[j]
            j = max(self.next[j], 0)
        return idxs
