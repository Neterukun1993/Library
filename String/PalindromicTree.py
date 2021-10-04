# PalindromicTree
# https://math314.hateblo.jp/entry/2016/12/19/005919

class Node:
    def __init__(self, length, count):
        self.length = length
        self.count = count
        self.suffix_link = 0
        self.link = {}


class PalindromicTree:
    def __init__(self):
        self.nodes = []
        self.string = []

        self.root_odd = Node(-1, 0)
        self.nodes.append(self.root_odd)
        self.root_even = Node(0, 0)
        self.nodes.append(self.root_even)
        self.cur = 0

    def prev_palindrome_node(self, idx):
        size = len(self.string) - 1
        while True:
            i = size - 1 - self.nodes[idx].length
            if i >= 0 and self.string[i] == self.string[-1]:
                break
            idx = self.nodes[idx].suffix_link
        return idx

    def add(self, char):
        self.string.append(char)
        idx = self.prev_palindrome_node(self.cur)

        if char in self.nodes[idx].link:
            self.cur = self.nodes[idx].link[char]
            self.nodes[self.cur].count += 1
            return

        self.nodes[idx].link[char] = len(self.nodes)
        new = Node(self.nodes[idx].length + 2, 1)
        self.nodes.append(new)
        self.cur = self.nodes[idx].link[char]

        if new.length == 1:
            new.suffix_link = 1
        else:
            idx = self.prev_palindrome_node(self.nodes[idx].suffix_link)
            new.suffix_link = self.nodes[idx].link[char]

    def frequency_build(self):
        n = len(self.nodes)
        frequency = [0] * n
        for i in reversed(range(n)):
            frequency[i] += self.nodes[i].count
            frequency[self.nodes[i].suffix_link] += frequency[i]
        return frequency
