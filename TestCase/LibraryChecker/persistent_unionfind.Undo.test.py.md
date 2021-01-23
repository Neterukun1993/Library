---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\UnionFindUndo.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.UnionFind.UnionFindUndo\
    \ import UnionFindUndo\r\n\r\n\r\ndef main():    \r\n    \"\"\"\u30AF\u30A8\u30EA\
    \u5148\u8AAD\u307F\u306B\u3088\u3063\u3066\u3001merge\u6642\u306B\u53C2\u7167\
    /\u751F\u6210\u3055\u308C\u308B\u30B0\u30E9\u30D5\u9593\u306B\u8FBA\u3092\u8CBC\
    \u308A\u3001\r\n    \u6728\u3092\u69CB\u7BC9\u3059\u308B\u3002\u305D\u306E\u5F8C\
    \u30AA\u30D5\u30E9\u30A4\u30F3\u30C0\u30A4\u30B3\u30CD\u3068\u540C\u69D8\u306E\
    \u8981\u9818\u3067\u30B7\u30DF\u30E5\u30EC\u30FC\u30C8\u3059\u308B\u3002\r\n \
    \   \"\"\"\r\n    n, q = map(int, input().split())\r\n    queries = [list(map(int,\
    \ input().split())) for i in range(q)]\r\n\r\n    tree = [[] for i in range(q)]\r\
    \n    judges = {}\r\n    merges = {}\r\n    for i, (flag, k, u, v) in enumerate(queries):\r\
    \n        if k == -1:\r\n            k = q - 1\r\n        if flag == 0:\r\n  \
    \          if i == q - 1:\r\n                continue\r\n            tree[i].append(k)\r\
    \n            tree[k].append(i)\r\n            merges[i] = (u, v)\r\n        else:\r\
    \n            if k not in judges:\r\n                judges[k] = []\r\n      \
    \      judges[k].append((i, u, v))\r\n\r\n    root = q - 1\r\n    visited = [False]\
    \ * q\r\n    visited[root] = True\r\n    idxs = [0] * q\r\n    stack = [root]\r\
    \n\r\n    # TODO: \u6728\u4E0A\u306E\u5DE1\u56DE\u3092\u30AA\u30A4\u30E9\u30FC\
    \u30C4\u30A2\u30FC\u3068\u3057\u3066\u30E9\u30A4\u30D6\u30E9\u30EA\u306B\u3059\
    \u308B\r\n    order = []\r\n    while True:\r\n        v = stack.pop()\r\n   \
    \     idx = idxs[v]\r\n        if idx == len(tree[v]):\r\n            break\r\n\
    \        if idx == 0:\r\n            order.append(v)\r\n        if visited[tree[v][idx]]\
    \ and idx == len(tree[v]) - 1:\r\n            order.append(v)\r\n            stack.append(tree[v][idx])\r\
    \n            tree[v][idx] += 1\r\n            continue\r\n        if visited[tree[v][idx]]:\r\
    \n            tree[v][idx], tree[v][idx + 1] = tree[v][idx + 1], tree[v][idx]\r\
    \n        visited[tree[v][idx]] = True\r\n        stack.append(tree[v][idx])\r\
    \n        idxs[v] += 1\r\n\r\n    ans = [-1] * q\r\n    visited = [False] * q\r\
    \n    uf = UnionFindUndo(n)\r\n    for i in order:\r\n        if i in merges:\r\
    \n            if visited[i]:\r\n                uf.undo()\r\n                continue\r\
    \n            else:\r\n                visited[i] = True\r\n                uf.merge(*merges[i])\r\
    \n        if i in judges:\r\n            for j, u, v in judges[i]:\r\n       \
    \         ans[j] = int(uf.same(u, v))\r\n\r\n    print('\\n'.join(map(str, [res\
    \ for res in ans if res != -1])))\r\n\r\n\r\nif __name__ == '__main__':\r\n  \
    \  main()\r\n"
  dependsOn:
  - DataStructure\UnionFind\UnionFindUndo.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\persistent_unionfind.Undo.test.py
  requiredBy: []
  timestamp: '2021-01-03 22:35:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\persistent_unionfind.Undo.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\persistent_unionfind.Undo.test.py
- /verify\TestCase\LibraryChecker\persistent_unionfind.Undo.test.py.html
title: TestCase\LibraryChecker\persistent_unionfind.Undo.test.py
---
