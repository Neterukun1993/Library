---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/SegmentTree/LazySegmentTree.py
    title: "\u9045\u5EF6\u4F1D\u64AD\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment\
      \ Tree with Lazy Propagation)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_affine_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_affine_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.LazySegmentTree\
    \ import LazySegmentTree\n\n\nMOD = 998244353\nMASK = (1 << 32) - 1\nunitA = 1\
    \ << 32\nunitX = 0\n\n\ndef X_f(x1, x2):\n    x = x1 + x2\n    return ((x >> 32)\
    \ % MOD << 32) + (x & MASK) % MOD\n\n\ndef XA_map(x, a):\n    x0, x1 = x >> 32,\
    \ x & MASK\n    a0, a1 = a >> 32, a & MASK\n    return (((x0 * a0 + x1 * a1) %\
    \ MOD) << 32) + x1\n\n\ndef A_f(a1, a2):\n    a10, a11 = a1 >> 32, a1 & MASK\n\
    \    a20, a21 = a2 >> 32, a2 & MASK\n    return ((a20 * a10 % MOD) << 32) + (a20\
    \ * a11 + a21) % MOD\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    lst = LazySegmentTree(n, unitX, unitA, X_f, A_f, XA_map)\n\
    \    lst.build([(val << 32) + 1 for val in a])\n\n    ans = []\n    for flag,\
    \ *query in queries:\n        if flag == 0:\n            l, r, b, c = query\n\
    \            if l + 1 == r:\n                lst.apply(l, (b << 32) + c)\n   \
    \         else:\n                lst.range_apply(l, r, (b << 32) + c)\n      \
    \  else:\n            l, r = query\n            if l + 1 == r:\n             \
    \   ans.append(lst[l] >> 32)\n            else:\n                ans.append(lst.fold(l,\
    \ r) >> 32)\n\n    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/LazySegmentTree.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/range_affine_range_sum.test.py
  requiredBy: []
  timestamp: '2021-01-17 15:49:23+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/range_affine_range_sum.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/range_affine_range_sum.test.py
- /verify/TestCase/LibraryChecker/range_affine_range_sum.test.py.html
title: TestCase/LibraryChecker/range_affine_range_sum.test.py
---
