---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/suffixarray.nlogn.test.py
    title: TestCase/LibraryChecker/suffixarray.nlogn.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SuffixArray:\n    def __init__(self, string):\n        self.n = len(string)\n\
    \        self.sa = [0] * (self.n + 1)\n        self.lcp = [0] * (self.n + 1)\n\
    \        if type(string[0]) == str:\n            array = [ord(char) for char in\
    \ string]\n        else:\n            array = string\n        array = self.compress(array)\n\
    \        self.build_SA(array)\n        self.build_LCP(array)\n\n    def compress(self,\
    \ array):\n        memo = {val: idx for idx, val in enumerate(sorted(set(array)))}\n\
    \        array = [memo[val] + 1 for val in array]\n        return array\n\n  \
    \  def build_SA(self, array):\n        array = array + [0]\n        n = len(array)\n\
    \        c = [0] * n\n        cnt = [0] * n\n        cn = [0] * n\n\n        for\
    \ val in array:\n            cnt[val] += 1\n        for i in range(1, n):\n  \
    \          cnt[i] += cnt[i - 1]\n        for i, val in enumerate(array):\n   \
    \         cnt[val] -= 1\n            self.sa[cnt[val]] = i\n\n        c[self.sa[0]]\
    \ = 0\n        classes = 1\n        for i in range(1, n):\n            if array[self.sa[i]]\
    \ != array[self.sa[i - 1]]:\n                classes += 1\n            c[self.sa[i]]\
    \ = classes - 1\n\n        k = 0\n        while (1 << k) < n:\n            shift\
    \ = 1 << k\n            pn = [(self.sa[i] - shift) % n for i in range(n)]\n\n\
    \            for i in range(classes):\n                cnt[i] = 0\n          \
    \  for i in pn:\n                cnt[c[i]] += 1\n            for i in range(1,\
    \ classes):\n                cnt[i] += cnt[i - 1]\n            for i in reversed(pn):\n\
    \                cnt[c[i]] -= 1\n                self.sa[cnt[c[i]]] = i\n\n  \
    \          prv_idx = self.sa[0]\n            cn[prv_idx] = 0\n            classes\
    \ = 1\n            for cur_idx in self.sa[1:]:\n                cur = c[cur_idx],\
    \ c[(cur_idx + shift) % n]\n                prv = c[prv_idx], c[(prv_idx + shift)\
    \ % n]\n                if cur != prv:\n                    classes += 1\n   \
    \             cn[cur_idx] = classes - 1\n                prv_idx = cur_idx\n \
    \           c, cn = cn, c\n            k += 1\n\n    def build_LCP(self, array):\n\
    \        rank = [0] * (self.n + 1)\n        for i, val in enumerate(self.sa):\n\
    \            rank[val] = i\n        h = 0\n        for i, rk in enumerate(rank):\n\
    \            j = self.sa[rk - 1]\n            if h > 0:\n                h -=\
    \ 1\n            while j + h < self.n and i + h < self.n:\n                if\
    \ array[j + h] != array[i + h]:\n                    break\n                else:\n\
    \                    h += 1\n            self.lcp[rk - 1] = h\n"
  dependsOn: []
  isVerificationFile: false
  path: String/SA_nlogn.py
  requiredBy: []
  timestamp: '2021-01-06 00:03:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/suffixarray.nlogn.test.py
documentation_of: String/SA_nlogn.py
layout: document
title: "\u63A5\u5C3E\u8F9E\u914D\u5217 ($\\mathrm{O}(N (\\log N))$)"
---
