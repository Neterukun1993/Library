---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.DAryHeap2.test.py
    title: TestCase/AOJ/ALDS1_9_C.DAryHeap2.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.DAryHeap3.test.py
    title: TestCase/AOJ/ALDS1_9_C.DAryHeap3.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.DAryHeap4.test.py
    title: TestCase/AOJ/ALDS1_9_C.DAryHeap4.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.DAryHeap8.test.py
    title: TestCase/AOJ/ALDS1_9_C.DAryHeap8.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DAryHeap:\n    def __init__(self, D=2):\n        self.heap = []\n \
    \       self.D = D\n\n    def __len__(self):\n        return len(self.heap)\n\n\
    \    @property\n    def min(self):\n        return self.heap[0]\n\n    def push(self,\
    \ val):\n        self.heap.append(val)\n        idx = len(self) - 1\n        par\
    \ = (idx - 1) // self.D\n        while par >= 0 and self.heap[idx] < self.heap[par]:\n\
    \            self.heap[idx], self.heap[par] = self.heap[par], self.heap[idx]\n\
    \            idx, par = par, (par - 1) // self.D\n\n    def pop(self):\n     \
    \   if not self:\n            raise IndexError('pop from empty heap')\n      \
    \  if len(self) == 1:\n            return self.heap.pop()\n        res = self.heap[0]\n\
    \        self.heap[0] = self.heap.pop()\n        idx = 0\n        while True:\n\
    \            min_val = self.heap[idx]\n            chi = -1\n            for i\
    \ in range(1, self.D + 1):\n                tmp_chi = idx * self.D + i\n     \
    \           if tmp_chi < len(self) and min_val > self.heap[tmp_chi]:\n       \
    \             min_val = self.heap[tmp_chi]\n                    chi = tmp_chi\n\
    \            if chi == -1:\n                break\n            if self.heap[idx]\
    \ > self.heap[chi]:\n                self.heap[idx], self.heap[chi] = self.heap[chi],\
    \ self.heap[idx]\n            idx = chi\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Heap/DAryHeap.py
  requiredBy: []
  timestamp: '2021-01-15 07:30:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_9_C.DAryHeap2.test.py
  - TestCase/AOJ/ALDS1_9_C.DAryHeap8.test.py
  - TestCase/AOJ/ALDS1_9_C.DAryHeap4.test.py
  - TestCase/AOJ/ALDS1_9_C.DAryHeap3.test.py
documentation_of: DataStructure/Heap/DAryHeap.py
layout: document
title: D-Ary Heap
---
## 概要
二分ヒープ (Binary Heap) を `D` 分木に拡張したヒープ。`D = 2` であれば Binary Heap、`D = 3` であれば Ternary Heap、`D = 4` であれば Quaternary Heap。子 `k` から親へのアクセスおよび親 `k` から子へのアクセスを添え字で表現できるため、配列上でヒープをシミュレートできる。

画像は D-Ary Heap の添字の様子。
![example](https://Neterukun1993.github.io/Library/DAryHeap-example.png)
![index](https://Neterukun1993.github.io/Library/DAryHeap-index.png)

## 使い方
`DAryHeap(D: int)`  
`D` 分木版の空の Binary Heap を作成する。計算量 $O(1)$

- `__len__() -> int`  
ヒープの大きさを返す。計算量 $O(1)$

- `min -> int`  
ヒープ内の最小の値を返す。計算量 $O(1)$

- `push(val: int) -> None`  
ヒープに `val` を追加する。計算量 $O(\log n / \log D)$

- `pop() -> int`  
ヒープ内の最小の値を削除してその値を返す。計算量 $O(D\log n / \log D$
