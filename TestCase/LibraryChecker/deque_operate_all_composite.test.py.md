---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/FoldableDeque.py
    title: FoldableDeque
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/deque_operate_all_composite
    links:
    - https://judge.yosupo.jp/problem/deque_operate_all_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/deque_operate_all_composite\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.FoldableDeque\
    \ import FoldableDeque\n\n\nMOD = 998244353\nMASK = (1 << 32) - 1\n\n\ndef X_f(x1,\
    \ x2):\n    x = x1 + x2\n    return ((x >> 32) % MOD << 32) + (x & MASK) % MOD\n\
    \n\ndef XA_map(x, a):\n    x0, x1 = x >> 32, x & MASK\n    a0, a1 = a >> 32, a\
    \ & MASK\n    return (((x0 * a0 + x1 * a1) % MOD) << 32) + x1\n\n\ndef A_f(a1,\
    \ a2):\n    a10, a11 = a1 >> 32, a1 & MASK\n    a20, a21 = a2 >> 32, a2 & MASK\n\
    \    return ((a20 * a10 % MOD) << 32) + (a20 * a11 + a21) % MOD\n\n\ndef main():\n\
    \    q = int(input())\n    queries = [list(map(int, input().split())) for i in\
    \ range(q)]\n\n    fd = FoldableDeque(A_f)\n    ans = []\n    for query in queries:\n\
    \        if query[0] == 0:\n            _, a, b = query\n            fd.appendleft((a\
    \ << 32) + b)\n        elif query[0] == 1:\n            _, a, b = query\n    \
    \        fd.append((a << 32) + b)\n        elif query[0] == 2:\n            fd.popleft()\n\
    \        elif query[0] == 3:\n            fd.pop()\n        else:\n          \
    \  _, x = query\n            if len(fd) == 0:\n                ans.append(x)\n\
    \            else:\n                a = fd.fold_all()\n                res = XA_map((x\
    \ << 32) + 1, a)\n                ans.append(res >> 32)\n\n    print('\\n'.join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/FoldableDeque.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/deque_operate_all_composite.test.py
  requiredBy: []
  timestamp: '2022-09-12 01:37:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/deque_operate_all_composite.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/deque_operate_all_composite.test.py
- /verify/TestCase/LibraryChecker/deque_operate_all_composite.test.py.html
title: TestCase/LibraryChecker/deque_operate_all_composite.test.py
---
