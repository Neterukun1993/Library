---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_C.BTree.test.py
    title: TestCase/AOJ/ITP2_7_C.BTree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left, bisect_right, insort\n\n\nclass BTreeNode:\n\
    \    def __init__(self, B_SIZE):\n        self.B_SIZE = B_SIZE\n        self.keys\
    \ = []\n        self.children = []\n\n    def split(self):\n        if len(self.keys)\
    \ != self.B_SIZE * 2:\n            return None\n        ptr = BTreeNode(self.B_SIZE)\n\
    \        ptr.keys, self.keys = self.keys[:self.B_SIZE], self.keys[self.B_SIZE:]\n\
    \        ptr.children, self.children = self.children[:self.B_SIZE], self.children[self.B_SIZE:]\n\
    \        return ptr\n\n    def shift_lr(self, idx):\n        ptrl, ptrr = self.children[idx],\
    \ self.children[idx + 1]\n        ptrr.keys.insert(0, ptrl.keys[-1])\n       \
    \ del ptrl.keys[-1]\n        if ptrl.children:\n            ptrr.children.insert(0,\
    \ ptrl.children[-1])\n            del ptrl.children[-1]\n        self.keys[idx],\
    \ ptrr.keys[0] = ptrr.keys[0], self.keys[idx]\n\n    def shift_rl(self, idx):\n\
    \        ptrl, ptrr = self.children[idx], self.children[idx + 1]\n        ptrl.keys.append(ptrr.keys[0])\n\
    \        del ptrr.keys[0]\n        if ptrr.children:\n            ptrl.children.append(ptrr.children[0])\n\
    \            del ptrr.children[0]\n        self.keys[idx], ptrl.keys[-1] = ptrl.keys[-1],\
    \ self.keys[idx]\n\n    def merge(self, idx):\n        self.children[idx].keys\
    \ += [self.keys[idx]] + self.children[idx + 1].keys\n        self.children[idx].children\
    \ += self.children[idx + 1].children\n        del self.keys[idx], self.children[idx\
    \ + 1]\n        assert(len(self.keys) + 1 == len(self.children))\n\n\nclass SortedSetBTree:\n\
    \    def __init__(self, B_SIZE=512):\n        self.B_SIZE = B_SIZE\n        self.root\
    \ = BTreeNode(self.B_SIZE)\n        self.size = 0\n\n    def __contains__(self,\
    \ key):\n        return self._search(key)\n\n    def __len__(self):\n        return\
    \ self.size\n\n    def __iter__(self):\n        return self._generate_rec(self.root)\n\
    \n    def _search(self, key):\n        ptr = self.root\n        while True:\n\
    \            idx = bisect_left(ptr.keys, key)\n            if idx != len(ptr.keys)\
    \ and ptr.keys[idx] == key:\n                return True\n            if not ptr.children:\n\
    \                return False\n            ptr = ptr.children[idx]\n\n    def\
    \ _generate_rec(self, ptr):\n        for idx, chi in enumerate(ptr.children):\n\
    \            yield from self._generate_rec(chi)\n            if idx < len(ptr.keys):\n\
    \                yield ptr.keys[idx]\n        if not ptr.children:\n         \
    \   for key in ptr.keys:\n                yield key\n\n    def _generate_rec_vl(self,\
    \ ptr, vl, f):\n        idxl = 0 if f else bisect_left(ptr.keys, vl)\n       \
    \ for idx, chi in enumerate(ptr.children[idxl:], idxl):\n            if idx ==\
    \ idxl:\n                yield from self._generate_rec_vl(chi, vl, f | False)\n\
    \            else:\n                yield from self._generate_rec_vl(chi, vl,\
    \ True)\n            if idx < len(ptr.keys):\n                yield ptr.keys[idx]\n\
    \        if not ptr.children:\n            for key in ptr.keys[idxl:]:\n     \
    \           yield key\n\n    def _add_rec(self, ptr, key):\n        if not ptr.children:\n\
    \            insort(ptr.keys, key)\n        else:\n            i = bisect_right(ptr.keys,\
    \ key)\n            p = self._add_rec(ptr.children[i], key)\n            if p\
    \ is not None:\n                ptr.keys.insert(i, p.keys.pop())\n           \
    \     ptr.children.insert(i, p)\n        return ptr.split()\n\n    def _remove_rec(self,\
    \ ptr, key):\n        idx = bisect_left(ptr.keys, key)\n        if idx != len(ptr.keys)\
    \ and ptr.keys[idx] == key:\n            if not ptr.children:\n              \
    \  del ptr.keys[idx]\n            else:\n                ptr.keys[idx] = self._remove_smallest(ptr.children[idx\
    \ + 1])\n                self._check_underflow(ptr, idx + 1)\n            return\
    \ True\n        elif ptr.children and self._remove_rec(ptr.children[idx], key):\n\
    \            self._check_underflow(ptr, idx)\n            return True\n      \
    \  return False\n\n    def _remove_smallest(self, ptr):\n        if not ptr.children:\n\
    \            res = ptr.keys[0]\n            del ptr.keys[0]\n            return\
    \ res\n        res = self._remove_smallest(ptr.children[0])\n        self._check_underflow(ptr,\
    \ 0)\n        return res\n\n    def _check_underflow(self, ptr, idx):\n      \
    \  if len(ptr.children[idx].keys) >= self.B_SIZE - 1:\n            return\n  \
    \      elif idx == 0:\n            if len(ptr.children[idx + 1].keys) > self.B_SIZE:\
    \ ptr.shift_rl(idx)\n            else: ptr.merge(idx)\n        else:\n       \
    \     if len(ptr.children[idx - 1].keys) > self.B_SIZE: ptr.shift_lr(idx - 1)\n\
    \            else: ptr.merge(idx - 1)\n\n    def add(self, key):\n        if key\
    \ in self:\n            return True\n        ptr = self.root\n        p = self._add_rec(ptr,\
    \ key)\n        if p is not None:\n            root = BTreeNode(self.B_SIZE)\n\
    \            root.keys = [p.keys.pop()]\n            root.children = [p, self.root]\n\
    \            self.root = root\n        self.size += 1\n        return True\n\n\
    \    def remove(self, key):\n        flag = self._remove_rec(self.root, key)\n\
    \        if len(self.root.children) == 1:\n            self.root = self.root.children[0]\n\
    \        if flag: self.size -= 1\n        return flag\n\n    def iterate(self,\
    \ vl):\n        return self._generate_rec_vl(self.root, vl, False)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetBTree.py
  requiredBy: []
  timestamp: '2021-02-07 17:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_C.BTree.test.py
documentation_of: DataStructure/SortedSet/SortedSetBTree.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (B-Tree)"
---

## 概要
B-Tree による順序付き集合。

## 使い方
`SortedSetBTree(B_SIZE=512)`  
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
