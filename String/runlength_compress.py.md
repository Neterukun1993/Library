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
  code: "def compress(string):\n    n = len(string)\n    begin, cnt = 0, 0\n    ans\
    \ = []\n    if n == 0:\n        return ans\n    for end in range(n + 1):\n   \
    \     if end == n or string[begin] != string[end]:\n            ans.append((string[begin],\
    \ cnt))\n            begin, cnt = end, 1\n        else:\n            cnt += 1\n\
    \    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: String/runlength_compress.py
  requiredBy: []
  timestamp: '2021-01-22 20:39:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/runlength_compress.py
layout: document
redirect_from:
- /library/String/runlength_compress.py
- /library/String/runlength_compress.py.html
title: String/runlength_compress.py
---
