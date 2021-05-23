class PatriciaNode:
    def __init__(self, string=None):
        self.data = string
        self.child = {}
        self.valid = False

    def set_child(self, string):
        self.child[string[0]] = PatriciaNode(string)
        return self.child[string[0]]

    def get_child(self, s):
        if s not in self.child:
            return None
        return self.child[s]


class Patricia:
    def __init__(self):
        self.root = PatriciaNode()

    def _longest_match(self, string):
        ptr = self.root
        i = 0
        while i < len(string):
            ptrch = ptr.get_child(string[i])
            if ptrch is None:
                break
            j = 1
            while j < len(ptrch .data):
                if i + j == len(string) or string[i + j] != ptrch.data[j]:
                    return ptrch, i + j, j
                j += 1
            i += j
            ptr = ptrch
        return ptr, i, 0

    def search(self, string):
        ptr, match, sub_match = self._longest_match(string)
        if len(string) == match and sub_match == 0:
            return ptr.valid
        return False

    def insert(self, string):
        ptr, match, sub_match = self._longest_match(string)
        if len(string) == match and sub_match == 0 and ptr.valid:
            return False
        if sub_match > 0:
            newptr = PatriciaNode(ptr.data[sub_match:])
            newptr.child = ptr.child
            newptr.valid = ptr.valid
            ptr.data = ptr.data[:sub_match]
            ptr.child = {newptr.data[0]: newptr}
            ptr.valid = False
        if match < len(string):
            ptr = ptr.set_child(string[match:])
        ptr.valid = True
        return True

    def delete(self, string):
        ptr, match, sub_match = self._longest_match(string)
        if len(string) == match and sub_match == 0 and ptr.valid:
            ptr.valid = False
            return True
        return False
