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
  code: "def encoding(s):\n    n = len(s)\n    begin, cnt = 0, 0\n    ans = []\n \
    \   if n == 0:\n        return ans\n    for end in range(n + 1):\n        if end\
    \ == n or s[begin] != s[end]:\n            ans.append((s[begin], cnt))\n     \
    \       begin, cnt = end, 1\n        else:\n            cnt += 1\n    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: String/run_length_encoding.py
  requiredBy: []
  timestamp: '2021-01-28 20:42:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/run_length_encoding.py
layout: document
title: "\u30E9\u30F3\u30EC\u30F3\u30B0\u30B9\u5727\u7E2E"
---
## 使い方
`encoding(s: Sequence[Any]) -> List[Tuple[Any, int]]`  
`s` 中の連続した同じ要素をまとめて (要素, 連続した回数) 変換した結果を返す。計算量 $O(n)$
