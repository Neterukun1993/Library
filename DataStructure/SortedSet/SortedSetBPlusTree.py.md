---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_C.BPlusTree.test.py
    title: TestCase/AOJ/ITP2_7_C.BPlusTree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left, insort\n\n\nclass BPlusTreeLeaf:\n    def\
    \ __init__(self, B_SIZE):\n        self.B_SIZE = B_SIZE\n        self.prev_node\
    \ = None\n        self.next_node = None\n        self.keys = []\n\n    def is_leaf(self):\n\
    \        return True\n\n    def split(self):\n        if len(self.keys) != self.B_SIZE\
    \ * 2:\n            return None\n        new = BPlusTreeLeaf(self.B_SIZE)\n  \
    \      new.keys, self.keys = self.keys[:self.B_SIZE], self.keys[self.B_SIZE:]\n\
    \        if self.prev_node is not None:\n            self.prev_node.next_node,\
    \ new.prev_node = new, self.prev_node\n        new.next_node, self.prev_node =\
    \ self, new\n        return new\n\n    def key_pop(self):\n        return self.keys[-1]\n\
    \n\nclass BPlusTreeInnerNode:\n    def __init__(self, B_SIZE):\n        self.B_SIZE\
    \ = B_SIZE\n        self.keys = []\n        self.children = []\n\n    def is_leaf(self):\n\
    \        return False\n\n    def split(self):\n        if len(self.keys) != self.B_SIZE\
    \ * 2:\n            return None\n        new = BPlusTreeInnerNode(self.B_SIZE)\n\
    \        new.keys, self.keys = self.keys[:self.B_SIZE], self.keys[self.B_SIZE:]\n\
    \        new.children, self.children = (self.children[:self.B_SIZE],\n       \
    \                                self.children[self.B_SIZE:])\n        return\
    \ new\n\n    def key_pop(self):\n        return self.keys.pop()\n\n    def shift_lr(self,\
    \ idx):\n        ptrl, ptrr = self.children[idx], self.children[idx + 1]\n   \
    \     ptrr.keys.insert(0, ptrl.keys.pop())\n        if ptrl.is_leaf():\n     \
    \       self.keys[idx] = ptrl.keys[-1]\n        else:\n            ptrr.children.insert(0,\
    \ ptrl.children.pop())\n            self.keys[idx], ptrr.keys[0] = ptrr.keys[0],\
    \ self.keys[idx]\n\n    def shift_rl(self, idx):\n        ptrl, ptrr = self.children[idx],\
    \ self.children[idx + 1]\n        ptrl.keys.append(ptrr.keys.pop(0))\n       \
    \ if ptrl.is_leaf():\n            self.keys[idx] = ptrl.keys[-1]\n        else:\n\
    \            ptrl.children.append(ptrr.children.pop(0))\n            self.keys[idx],\
    \ ptrl.keys[-1] = ptrl.keys[-1], self.keys[idx]\n\n    def merge(self, idx):\n\
    \        if self.children[idx].is_leaf():\n            self.children[idx].keys\
    \ += self.children[idx + 1].keys\n            self.children[idx].next_node = self.children[idx\
    \ + 1].next_node\n            if self.children[idx + 1].next_node is not None:\n\
    \                self.children[idx + 1].next_node.prev_node = self.children[idx]\n\
    \        else:\n            self.children[idx].keys += ([self.keys[idx]]\n   \
    \                                     + self.children[idx + 1].keys)\n       \
    \     self.children[idx].children += self.children[idx + 1].children\n       \
    \ del self.keys[idx], self.children[idx + 1]\n\n\nclass SortedSetBPlusTree:\n\
    \    def __init__(self, B_SIZE=512):\n        self.B_SIZE = B_SIZE\n        self.root\
    \ = BPlusTreeLeaf(self.B_SIZE)\n        self.size = 0\n\n    def __contains__(self,\
    \ key):\n        return self._search(key)\n\n    def __len__(self):\n        return\
    \ self.size\n\n    def __iter__(self):\n        ptr = self.root\n        while\
    \ not ptr.is_leaf():\n            ptr = ptr.children[0]\n        while ptr is\
    \ not None:\n            for key in ptr.keys:\n                yield key\n   \
    \         ptr = ptr.next_node\n\n    def _search(self, key):\n        ptr = self.root\n\
    \        while not ptr.is_leaf():\n            idx = bisect_left(ptr.keys, key)\n\
    \            ptr = ptr.children[idx]\n        idx = bisect_left(ptr.keys, key)\n\
    \        return idx != len(ptr.keys) and ptr.keys[idx] == key\n\n    def _add_rec(self,\
    \ ptr, key):\n        if ptr.is_leaf():\n            insort(ptr.keys, key)\n \
    \       else:\n            idx = bisect_left(ptr.keys, key)\n            p = self._add_rec(ptr.children[idx],\
    \ key)\n            if p is not None:\n                ptr.keys.insert(idx, p.key_pop())\n\
    \                ptr.children.insert(idx, p)\n        return ptr.split()\n\n \
    \   def _remove_rec(self, ptr, key):\n        idx = bisect_left(ptr.keys, key)\n\
    \        if ptr.is_leaf():\n            if idx != len(ptr.keys) and ptr.keys[idx]\
    \ == key:\n                del ptr.keys[idx]\n                return True\n  \
    \          return False\n        elif self._remove_rec(ptr.children[idx], key):\n\
    \            self._check_underflow(ptr, idx)\n            return True\n      \
    \  return False\n\n    def _check_underflow(self, ptr, idx):\n        if len(ptr.children[idx].keys)\
    \ >= self.B_SIZE - 1:\n            pass\n        elif idx == 0:\n            if\
    \ len(ptr.children[idx + 1].keys) > self.B_SIZE:\n                ptr.shift_rl(idx)\n\
    \            else:\n                ptr.merge(idx)\n        else:\n          \
    \  if len(ptr.children[idx - 1].keys) > self.B_SIZE:\n                ptr.shift_lr(idx\
    \ - 1)\n            else:\n                ptr.merge(idx - 1)\n\n    def add(self,\
    \ key):\n        if key in self:\n            return False\n        ptrr = self.root\n\
    \        ptrl = self._add_rec(self.root, key)\n        if ptrl is not None:\n\
    \            root = BPlusTreeInnerNode(self.B_SIZE)\n            root.keys = [ptrl.key_pop()]\n\
    \            root.children = [ptrl, ptrr]\n            self.root = root\n    \
    \    self.size += 1\n        return True\n\n    def remove(self, key):\n     \
    \   removed = self._remove_rec(self.root, key)\n        if not self.root.is_leaf()\
    \ and len(self.root.children) == 1:\n            self.root = self.root.children[0]\n\
    \        self.size -= int(removed)\n        return removed\n\n    def iterate(self,\
    \ keyl):\n        ptr = self.root\n        while not ptr.is_leaf():\n        \
    \    idx = bisect_left(ptr.keys, keyl)\n            ptr = ptr.children[idx]\n\
    \        for key in ptr.keys[bisect_left(ptr.keys, keyl):]:\n            yield\
    \ key\n        ptr = ptr.next_node\n        while ptr is not None:\n         \
    \   for key in ptr.keys:\n                yield key\n            ptr = ptr.next_node\n\
    \n    def prev_val(self, upper):\n        ptr = self.root\n        while not ptr.is_leaf():\n\
    \            idx = bisect_left(ptr.keys, upper)\n            ptr = ptr.children[idx]\n\
    \        idx = bisect_left(ptr.keys, upper)\n        if idx > 0:\n           \
    \ return ptr.keys[idx - 1]\n        elif ptr.prev_node is not None:\n        \
    \    return ptr.prev_node.keys[-1]\n        return None\n\n    def next_val(self,\
    \ lower):\n        ptr = self.root\n        while not ptr.is_leaf():\n       \
    \     idx = bisect_left(ptr.keys, lower)\n            ptr = ptr.children[idx]\n\
    \        idx = bisect_left(ptr.keys, lower)\n        if idx < len(ptr.keys):\n\
    \            return ptr.keys[idx]\n        elif ptr.next_node is not None:\n \
    \           return ptr.next_node.keys[0]\n        return None\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetBPlusTree.py
  requiredBy: []
  timestamp: '2021-09-04 22:53:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_C.BPlusTree.test.py
documentation_of: DataStructure/SortedSet/SortedSetBPlusTree.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (B+Tree)"
---

## 概要
B+Tree による順序付き集合。

## 使い方
`SortedSetBPlusTree(B_SIZE=512)`  
空の順序付き集合を作成する。計算量 $O(1)$

- `__contains__(key: int) -> bool`  
要素 `key` が集合に属しているかどうかを返す。計算量 $O(\log n)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[int]`  
要素の小さい順のイテレータオブジェクトを返す。オブジェクト生成の計算量 $O(1)$

- `add(key: int) -> bool`  
要素 `key` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `key` が集合に属していた場合) は `False` を返す。計算量 $O(\log n)$

- `remove(key: int) -> bool`  
集合から `key` を削除する。削除に成功した場合は `True` を、失敗した場合 (`key` が集合に属していなかった場合) は `False` を返す。計算量 $O(\log n)$

- `iterate(vl: int) -> Iterator[int]`  
`vl` 以上の要素に対して、小さい順のイテレータオブジェクトを返す。オブジェクト生成の計算量 $O(1)$

- `next_val(lower: int) -> int`
`lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$

- `prev_val(upper: int) -> int`
`upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$
