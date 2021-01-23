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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RadixHeap:\r\n    def __init__(self, LIMIT):\r\n        self.LIMIT\
    \ = LIMIT\r\n        self.vals = [[] for i in range(LIMIT.bit_length() + 1)]\r\
    \n        self.size = 0\r\n        self.last = 0\r\n\r\n    def __len__(self):\r\
    \n        return self.size\r\n\r\n    def push(self, key, val):\r\n        if\
    \ key > self.LIMIT:\r\n            raise RuntimeError(f'A pushed value {x} must\
    \ be no more than {self.LIMIT}')\r\n        if self.last > key:\r\n          \
    \  raise RuntimeError(f'A pushed value {x} must be not less than the last poped\
    \ value')\r\n        self.size += 1\r\n        self.vals[(key ^ self.last).bit_length()].append((key,\
    \ val))\r\n\r\n    def pop(self):\r\n        if self.size == 0:\r\n          \
    \  raise IndexError('pop from empty heapq')\r\n        if not self.vals[0]:\r\n\
    \            i = 1\r\n            while not self.vals[i]:\r\n                i\
    \ += 1\r\n            self.last = min([key for key, _ in self.vals[i]])\r\n  \
    \          for key, val in self.vals[i]:\r\n                self.vals[(key ^ self.last).bit_length()].append((key,\
    \ val))\r\n            self.vals[i] = []\r\n        self.size -= 1\r\n       \
    \ return self.vals[0].pop()\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\Heap\RadixHeap.py
  requiredBy: []
  timestamp: '2021-01-22 20:25:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure\Heap\RadixHeap.py
layout: document
redirect_from:
- /library\DataStructure\Heap\RadixHeap.py
- /library\DataStructure\Heap\RadixHeap.py.html
title: DataStructure\Heap\RadixHeap.py
---
