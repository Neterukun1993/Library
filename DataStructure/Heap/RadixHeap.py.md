---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RadixHeap:\n    def __init__(self, LIMIT):\n        self.LIMIT = LIMIT\n\
    \        self.vals = [[] for i in range(LIMIT.bit_length() + 1)]\n        self.size\
    \ = 0\n        self.last = 0\n\n    def __len__(self):\n        return self.size\n\
    \n    def push(self, key, val):\n        if key > self.LIMIT:\n            raise\
    \ RuntimeError(f'A pushed value {x} must be no more than {self.LIMIT}')\n    \
    \    if self.last > key:\n            raise RuntimeError(f'A pushed value {x}\
    \ must be not less than the last poped value')\n        self.size += 1\n     \
    \   self.vals[(key ^ self.last).bit_length()].append((key, val))\n\n    def pop(self):\n\
    \        if self.size == 0:\n            raise IndexError('pop from empty heapq')\n\
    \        if not self.vals[0]:\n            i = 1\n            while not self.vals[i]:\n\
    \                i += 1\n            self.last = min([key for key, _ in self.vals[i]])\n\
    \            for key, val in self.vals[i]:\n                self.vals[(key ^ self.last).bit_length()].append((key,\
    \ val))\n            self.vals[i] = []\n        self.size -= 1\n        return\
    \ self.vals[0].pop()\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Heap/RadixHeap.py
  requiredBy: []
  timestamp: '2021-01-22 20:25:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/Heap/RadixHeap.py
layout: document
redirect_from:
- /library/DataStructure/Heap/RadixHeap.py
- /library/DataStructure/Heap/RadixHeap.py.html
title: DataStructure/Heap/RadixHeap.py
---
