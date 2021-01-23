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
  code: "def compress(string):\r\n    n = len(string)\r\n    begin, cnt = 0, 0\r\n\
    \    ans = []\r\n    if n == 0:\r\n        return ans\r\n    for end in range(n\
    \ + 1):\r\n        if end == n or string[begin] != string[end]:\r\n          \
    \  ans.append((string[begin], cnt))\r\n            begin, cnt = end, 1\r\n   \
    \     else:\r\n            cnt += 1\r\n    return ans\r\n"
  dependsOn: []
  isVerificationFile: false
  path: String\runlength_compress.py
  requiredBy: []
  timestamp: '2021-01-22 20:39:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String\runlength_compress.py
layout: document
redirect_from:
- /library\String\runlength_compress.py
- /library\String\runlength_compress.py.html
title: String\runlength_compress.py
---
