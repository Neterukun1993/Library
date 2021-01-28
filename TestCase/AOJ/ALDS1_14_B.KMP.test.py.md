---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: String/KMP.py
    title: "KMP\u6CD5 (Knuth-Morrison-Pratt\u306E\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0\
      )"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B\n\
    from String.KMP import KMP\n\n\ndef main():\n    t = input()\n    p = input()\n\
    \n    kmp = KMP(p)\n    ans = kmp.match(t)\n    print('\\n'.join(map(str, ans)))\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - String/KMP.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_14_B.KMP.test.py
  requiredBy: []
  timestamp: '2021-01-28 22:51:39+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_14_B.KMP.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_14_B.KMP.test.py
- /verify/TestCase/AOJ/ALDS1_14_B.KMP.test.py.html
title: TestCase/AOJ/ALDS1_14_B.KMP.test.py
---
