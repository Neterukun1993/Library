class BinaryTrieNode:
    def __init__(self):
        self.bit0 = None
        self.bit1 = None
        self.size = 0


class BinaryTrie:
    def __init__(self, MAX_BIT_LENGTH=32):
        self.MAX_BIT_LENGTH = MAX_BIT_LENGTH
        self.root = BinaryTrieNode()

    def _generate_bit(self, val):
        for i in reversed(range(self.MAX_BIT_LENGTH)):
            yield (val >> i) & 1

    def search(self, val: int) -> bool:
        ptr = self.root
        for bit in self._generate_bit(val):
            if bit:
                ptr = ptr.bit1
            else:
                ptr = ptr.bit0
            if ptr is None:
                return False
        return True

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        ptr = self.root
        ptr.size += 1
        for bit in self._generate_bit(val):
            if bit:
                if ptr.bit1 is None:
                    ptr.bit1 = BinaryTrieNode()
                ptr = ptr.bit1
            else:
                if ptr.bit0 is None:
                    ptr.bit0 = BinaryTrieNode()
                ptr = ptr.bit0
            ptr.size += 1
        return True

    def delete(self, val: int) -> bool:
        if not self.search(val):
            return False
        ptr = self.root
        ptr.size -= 1
        for bit in self._generate_bit(val):
            if bit:
                if ptr.bit1.size == 1:
                    ptr.bit1 = None
                    return True
                ptr = ptr.bit1
            else:
                if ptr.bit0.size == 1:
                    ptr.bit0 = None
                    return True
                ptr = ptr.bit0
            ptr.size -= 1
        return True

    def get_xor_min(self, xor_val: int) -> int:
        ptr = self.root
        res = 0
        i = self.MAX_BIT_LENGTH
        for bit in self._generate_bit(xor_val):
            i -= 1
            if bit:
                if ptr.bit1 is not None:
                    ptr = ptr.bit1
                else:
                    ptr = ptr.bit0
                    res |= 1 << i
            else:
                if ptr.bit0 is not None:
                    ptr = ptr.bit0
                else:
                    ptr = ptr.bit1
                    res |= 1 << i
        return res
