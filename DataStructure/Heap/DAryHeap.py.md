---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_9_C.DAryHeap2.test.py
    title: TestCase\AOJ\ALDS1_9_C.DAryHeap2.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_9_C.DAryHeap3.test.py
    title: TestCase\AOJ\ALDS1_9_C.DAryHeap3.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_9_C.DAryHeap4.test.py
    title: TestCase\AOJ\ALDS1_9_C.DAryHeap4.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_9_C.DAryHeap8.test.py
    title: TestCase\AOJ\ALDS1_9_C.DAryHeap8.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DAryHeap:\r\n    def __init__(self, D=2):\r\n        self.heap = []\r\
    \n        self.D = D\r\n\r\n    def __len__(self):\r\n        return len(self.heap)\r\
    \n\r\n    @property\r\n    def min(self):\r\n        return self.heap[0]\r\n\r\
    \n    def push(self, val):\r\n        self.heap.append(val)\r\n        idx = len(self)\
    \ - 1\r\n        par = (idx - 1) // self.D\r\n        while par >= 0 and self.heap[idx]\
    \ < self.heap[par]:\r\n            self.heap[idx], self.heap[par] = self.heap[par],\
    \ self.heap[idx]\r\n            idx, par = par, (par - 1) // self.D\r\n\r\n  \
    \  def pop(self):\r\n        if not self:\r\n            raise IndexError('pop\
    \ from empty heap')\r\n        if len(self) == 1:\r\n            return self.heap.pop()\r\
    \n        res = self.heap[0]\r\n        self.heap[0] = self.heap.pop()\r\n   \
    \     idx = 0\r\n        while True:\r\n            min_val = self.heap[idx]\r\
    \n            chi = -1\r\n            for i in range(1, self.D + 1):\r\n     \
    \           tmp_chi = idx * self.D + i\r\n                if tmp_chi < len(self)\
    \ and min_val > self.heap[tmp_chi]:\r\n                    min_val = self.heap[tmp_chi]\r\
    \n                    chi = tmp_chi\r\n            if chi == -1:\r\n         \
    \       break\r\n            if self.heap[idx] > self.heap[chi]:\r\n         \
    \       self.heap[idx], self.heap[chi] = self.heap[chi], self.heap[idx]\r\n  \
    \          idx = chi\r\n        return res\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\Heap\DAryHeap.py
  requiredBy: []
  timestamp: '2021-01-15 07:30:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\ALDS1_9_C.DAryHeap2.test.py
  - TestCase\AOJ\ALDS1_9_C.DAryHeap3.test.py
  - TestCase\AOJ\ALDS1_9_C.DAryHeap4.test.py
  - TestCase\AOJ\ALDS1_9_C.DAryHeap8.test.py
documentation_of: DataStructure\Heap\DAryHeap.py
layout: document
title: D-Ary Heap
---
