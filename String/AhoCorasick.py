from collections import deque


class Node:
    def __init__(self):
        self.child = {}
        self.failure = None
        self.valid = 0

    def set_child(self, s):
        self.child[s] = Node()

    def get_child(self, s):
        if s not in self.child:
            return None
        return self.child[s]


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def add(self, pattern):
        ptr = self.root
        for s in pattern:
            if ptr.get_child(s) is None:
                ptr.set_child(s)
            ptr = ptr.get_child(s)
        ptr.valid += 1

    def build_pma(self):
        queue = deque()
        for s in self.root.child:
            ptrch = self.root.child[s]
            ptrch.failure = self.root
            queue.append(ptrch)
        while queue:
            ptr = queue.popleft()
            ptr.valid += ptr.failure.valid
            for s in ptr.child:
                ptrch = ptr.child[s]
                f = ptr.failure
                while f is not None and f.get_child(s) is None:
                    f = f.failure
                ptrch.failure = f.get_child(s) if f is not None else self.root
                queue.append(ptrch)

    def match_count(self, text):
        ptr = self.root
        res = 0
        for s in text:
            while ptr is not None and ptr.get_child(s) is None:
                ptr = ptr.failure
            ptr = ptr.get_child(s) if ptr is not None else self.root
            res += ptr.valid
        return res
