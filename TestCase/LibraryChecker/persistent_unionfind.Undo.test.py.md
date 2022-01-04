---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/UnionFindUndo.py
    title: "\u5DFB\u304D\u623B\u3057\u53EF\u80FDUnion Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/persistent_unionfind
    links:
    - https://judge.yosupo.jp/problem/persistent_unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.UnionFind.UnionFindUndo\
    \ import UnionFindUndo\n\n\ndef main():    \n    \"\"\"\u30AF\u30A8\u30EA\u5148\
    \u8AAD\u307F\u306B\u3088\u3063\u3066\u3001merge\u6642\u306B\u53C2\u7167/\u751F\
    \u6210\u3055\u308C\u308B\u30B0\u30E9\u30D5\u9593\u306B\u8FBA\u3092\u8CBC\u308A\
    \u3001\n    \u6728\u3092\u69CB\u7BC9\u3059\u308B\u3002\u305D\u306E\u5F8C\u30AA\
    \u30D5\u30E9\u30A4\u30F3\u30C0\u30A4\u30B3\u30CD\u3068\u540C\u69D8\u306E\u8981\
    \u9818\u3067\u30B7\u30DF\u30E5\u30EC\u30FC\u30C8\u3059\u308B\u3002\n    \"\"\"\
    \n    n, q = map(int, input().split())\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    tree = [[] for i in range(q)]\n    judges = {}\n \
    \   merges = {}\n    for i, (flag, k, u, v) in enumerate(queries):\n        if\
    \ k == -1:\n            k = q - 1\n        if flag == 0:\n            if i ==\
    \ q - 1:\n                continue\n            tree[i].append(k)\n          \
    \  tree[k].append(i)\n            merges[i] = (u, v)\n        else:\n        \
    \    if k not in judges:\n                judges[k] = []\n            judges[k].append((i,\
    \ u, v))\n\n    root = q - 1\n    visited = [False] * q\n    visited[root] = True\n\
    \    idxs = [0] * q\n    stack = [root]\n\n    # TODO: \u6728\u4E0A\u306E\u5DE1\
    \u56DE\u3092\u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC\u3068\u3057\u3066\u30E9\
    \u30A4\u30D6\u30E9\u30EA\u306B\u3059\u308B\n    order = []\n    while True:\n\
    \        v = stack.pop()\n        idx = idxs[v]\n        if idx == len(tree[v]):\n\
    \            break\n        if idx == 0:\n            order.append(v)\n      \
    \  if visited[tree[v][idx]] and idx == len(tree[v]) - 1:\n            order.append(v)\n\
    \            stack.append(tree[v][idx])\n            tree[v][idx] += 1\n     \
    \       continue\n        if visited[tree[v][idx]]:\n            tree[v][idx],\
    \ tree[v][idx + 1] = tree[v][idx + 1], tree[v][idx]\n        visited[tree[v][idx]]\
    \ = True\n        stack.append(tree[v][idx])\n        idxs[v] += 1\n\n    ans\
    \ = [-1] * q\n    visited = [False] * q\n    uf = UnionFindUndo(n)\n    for i\
    \ in order:\n        if i in merges:\n            if visited[i]:\n           \
    \     uf.undo()\n                continue\n            else:\n               \
    \ visited[i] = True\n                uf.merge(*merges[i])\n        if i in judges:\n\
    \            for j, u, v in judges[i]:\n                ans[j] = int(uf.same(u,\
    \ v))\n\n    print('\\n'.join(map(str, [res for res in ans if res != -1])))\n\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFindUndo.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/persistent_unionfind.Undo.test.py
  requiredBy: []
  timestamp: '2021-01-03 22:35:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/persistent_unionfind.Undo.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/persistent_unionfind.Undo.test.py
- /verify/TestCase/LibraryChecker/persistent_unionfind.Undo.test.py.html
title: TestCase/LibraryChecker/persistent_unionfind.Undo.test.py
---
