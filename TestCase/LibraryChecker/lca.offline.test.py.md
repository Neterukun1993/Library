---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/offline_lca.py
    title: "\u6700\u5C0F\u5171\u901A\u7956\u5148 (Tarjan \u306E\u30AA\u30D5\u30E9\u30A4\
      \u30F3\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\nimport\
    \ sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Tree.offline_lca import\
    \ offline_lca\n\n\ndef main():\n    n, q = map(int, input().split())\n    p =\
    \ list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    tree = [[] for i in range(n)]\n    for u, v in enumerate(p):\n\
    \        u += 1\n        tree[u].append(v)\n        tree[v].append(u)\n\n    ans\
    \ = offline_lca(tree, queries, 0)\n    print('\\n'.join(map(str, ans)))\n\n\n\
    if __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/offline_lca.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/lca.offline.test.py
  requiredBy: []
  timestamp: '2021-06-20 02:02:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/lca.offline.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/lca.offline.test.py
- /verify/TestCase/LibraryChecker/lca.offline.test.py.html
title: TestCase/LibraryChecker/lca.offline.test.py
---
