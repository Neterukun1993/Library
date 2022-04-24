---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RSQ_RMultipleQ.py
    title: RSQ_RMultipleQ
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc221/tasks/abc221_e
    links:
    - https://atcoder.jp/contests/abc221/tasks/abc221_e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc221/tasks/abc221_e\n\
    \nimport sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.RSQ_RMultipleQ\
    \ import RSQ_RMultipleQ\n\n\ndef main():\n    MOD = 998244353\n    n = int(input())\n\
    \    a = list(map(int, input().split()))\n\n    mapping = {val: i for i, val in\
    \ enumerate(sorted(set(a)))}\n    m = len(mapping)\n    st = RSQ_RMultipleQ(m)\n\
    \n    ans = 0\n    for val in a:\n        idx = mapping[val]\n        ans += st.fold(0,\
    \ idx + 1)\n        ans %= MOD\n\n        st.range_apply(0, m, 2)\n        st[idx]\
    \ = st[idx] + 1\n\n    print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/RSQ_RMultipleQ.py
  isVerificationFile: true
  path: TestCase/AtCoder/abc221_e.test.py
  requiredBy: []
  timestamp: '2022-04-24 23:38:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AtCoder/abc221_e.test.py
layout: document
redirect_from:
- /verify/TestCase/AtCoder/abc221_e.test.py
- /verify/TestCase/AtCoder/abc221_e.test.py.html
title: TestCase/AtCoder/abc221_e.test.py
---
