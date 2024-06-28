---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_14_B.KMP.test.py
    title: TestCase/AOJ/ALDS1_14_B.KMP.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class KMP:\n    def __init__(self, pattern):\n        self.pattern = pattern\n\
    \        self.next = [0] * (len(pattern) + 1)\n        self.next[0] = -1\n   \
    \     j = -1\n        for i in range(len(pattern)):\n            while j >= 0\
    \ and pattern[i] != pattern[j]:\n                j = self.next[j]\n          \
    \  j += 1\n            if i + 1 < len(pattern) and pattern[i + 1] == pattern[j]:\n\
    \                self.next[i + 1] = self.next[j]\n            else:\n        \
    \        self.next[i + 1] = j\n\n    def match(self, text):\n        idxs = []\n\
    \        i, j = 0, 0\n        while i + j < len(text):\n            if self.pattern[j]\
    \ == text[i + j]:\n                j += 1\n                if j != len(self.pattern):\n\
    \                    continue\n                idxs.append(i)\n            i +=\
    \ j - self.next[j]\n            j = max(self.next[j], 0)\n        return idxs\n"
  dependsOn: []
  isVerificationFile: false
  path: String/KMP.py
  requiredBy: []
  timestamp: '2021-01-28 22:51:39+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_14_B.KMP.test.py
documentation_of: String/KMP.py
layout: document
title: "KMP\u6CD5 (Knuth-Morrison-Pratt\u306E\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0)"
---

## 使い方
`KMP(pattern: Sequence[Any])`  
検索する文字列パターン `pattern` に対して前計算する。`n = len(pattern)` としたとき、計算量 $O(n)$

- `match(text: Sequence[Any]) -> List[int]`  
全文 `text` に対して、`pattern` と一致する `text` 中のインデックスの配列を返す。`m = len(text)` としたとき、計算量 $O(m + n)$
