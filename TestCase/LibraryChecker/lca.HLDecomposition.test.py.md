---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: Graph/Tree/HLDecomposition.py
    title: "HL\u5206\u89E3 (Heavy-Light Decomposition)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\nimport\
    \ sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Tree.HLDecomposition import\
    \ HLDecomposition\n\n\ndef main():\n    n, q = map(int, input().split())\n   \
    \ p = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    tree = [[] for i in range(n)]\n    for u, v in enumerate(p):\n\
    \        u += 1\n        tree[u].append(v)\n        tree[v].append(u)\n\n    hld\
    \ = HLDecomposition(tree)\n    ans = []\n    for u, v in queries:\n        ans.append(hld.lca(u,\
    \ v))\n\n    print('\\n'.join(map(str, ans)))\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Graph/Tree/HLDecomposition.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/lca.HLDecomposition.test.py
  requiredBy: []
  timestamp: '2021-01-16 04:24:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/lca.HLDecomposition.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/lca.HLDecomposition.test.py
- /verify/TestCase/LibraryChecker/lca.HLDecomposition.test.py.html
title: TestCase/LibraryChecker/lca.HLDecomposition.test.py
---
