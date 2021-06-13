class SuffixAutomaton:
    def __init__(self):
        self.last = 0
        self.next = [{}]
        self.link = [-1]
        self.length = [0]

    def _add_node(self, link, length):
        self.next.append({})
        self.link.append(link)
        self.length.append(length)

    def push(self, char):
        nxt, link, length = self.next, self.link, self.length
        new_node = len(nxt)
        self._add_node(-1, length[self.last] + 1)
        p = self.last
        while p != -1 and char not in nxt[p]:
            nxt[p][char] = new_node
            p = link[p]
        q = 0 if p == -1 else nxt[p][char]
        if p == -1 or length[p] + 1 == length[q]:
            link[new_node] = q
        else:
            new_q = len(nxt)
            self._add_node(link[q], length[p] + 1)
            nxt[-1] = {c: nxt[q][c] for c in nxt[q]}
            link[q] = link[new_node] = new_q
            while p != -1 and nxt[p][char] == q:
                nxt[p][char] = new_q
                p = link[p]
        self.last = new_node

    def has_substring(self, pattern):
        p = 0
        for char in pattern:
            if char not in self.next[p]:
                return False
            p = self.next[p][char]
        return True

    def number_of_substrings(self):
        ans = 0
        for i in range(1, len(self.length)):
            ans += self.length[i] - self.length[self.link[i]]
        return ans
