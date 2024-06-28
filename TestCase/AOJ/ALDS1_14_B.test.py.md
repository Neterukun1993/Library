---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: String/RollingHash.py
    title: "\u30ED\u30FC\u30EA\u30F3\u30B0\u30CF\u30C3\u30B7\u30E5"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B\n\
    from String.RollingHash import RollingHash\n\n\ndef main():\n    t = input()\n\
    \    p = input()\n\n    rht = RollingHash(t)\n    rhp = RollingHash(p)\n    for\
    \ l in range(len(t)):\n        r = l + len(p)\n        if r <= len(t) and rht.get_hash(l,\
    \ r) == rhp.get_hash(0, len(p)):\n            print(l)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - String/RollingHash.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_14_B.test.py
  requiredBy: []
  timestamp: '2021-01-23 23:52:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_14_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_14_B.test.py
- /verify/TestCase/AOJ/ALDS1_14_B.test.py.html
title: TestCase/AOJ/ALDS1_14_B.test.py
---
