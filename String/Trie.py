class TrieNode:
    def __init__(self):
        self.child = {}
        self.valid = False

    def set_child(self, s):
        self.child[s] = TrieNode()

    def get_child(self, s):
        if s not in self.child:
            return None
        return self.child[s]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, string):
        ptr = self.root
        for s in string:
            if ptr.get_child(s) is None:
                return False
            ptr = ptr.get_child(s)
        return ptr.valid

    def insert(self, string):
        ptr = self.root
        for s in string:
            if ptr.get_child(s) is None:
                ptr.set_child(s)
            ptr = ptr.get_child(s)
        if ptr.valid:
            return False
        ptr.valid = True
        return True

    def delete(self, string):
        ptr = self.root
        for s in string:
            if ptr.get_child(s) is None:
                return False
            ptr = ptr.get_child(s)
        ptr.valid = False
        return True
