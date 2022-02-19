---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/topological_sorted.py
    title: "\u6728\u4E0A\u306E\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/vertex_add_subtree_sum.dsu_on_tree.test.py
    title: TestCase/LibraryChecker/vertex_add_subtree_sum.dsu_on_tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph.Tree.topological_sorted import topological_sorted\n\n\ndef dsu_on_tree(tree,\
    \ root, add, sub, query):\n    n = len(tree)\n    tp_order, par = topological_sorted(tree,\
    \ root)\n\n    # 1.\u6709\u5411\u6728\u306E\u69CB\u7BC9\n    di_tree = [[] for\
    \ i in range(n)]\n    for v in range(n):\n        for nxt_v in tree[v]:\n    \
    \        if nxt_v == par[v]:\n                continue\n            di_tree[v].append(nxt_v)\n\
    \n    # 2.\u90E8\u5206\u6728\u30B5\u30A4\u30BA\u306E\u8A08\u7B97\n    sub_size\
    \ = [1] * n\n    for v in tp_order[::-1]:\n        for nxt_v in di_tree[v]:\n\
    \            sub_size[v] += sub_size[nxt_v]\n\n    # 3.\u6709\u5411\u6728\u306E\
    DFS\u884C\u304D\u304C\u3051\u9806\u306E\u69CB\u7BC9\n    di_tree = [sorted(tr,\
    \ key=lambda v: sub_size[v]) for tr in di_tree]\n    keeps = [0] * n\n    for\
    \ v in range(n):\n        di_tree[v] = di_tree[v][:-1][::-1] + di_tree[v][-1:]\n\
    \        for chi_v in di_tree[v][-1:]:\n            keeps[chi_v] = 1\n    tp_order,\
    \ _ = topological_sorted(di_tree, root)\n\n    # \u90E8\u5206\u6728\u304B\u3089\
    \u306E\u52A0\u7B97\u3082\u3057\u304F\u306F\u6E1B\u7B97\n    def calc(sub_root,\
    \ is_add):\n        stack = [sub_root]\n        while stack:\n            v =\
    \ stack.pop()\n            add(v) if is_add else sub(v)\n            for chi_v\
    \ in di_tree[v]:\n                stack.append(chi_v)\n\n    # 4.\u6709\u5411\u6728\
    \u306EDFS\u5E30\u308A\u304C\u3051\u9806\u3067\u9802\u70B9v\u306E\u90E8\u5206\u6728\
    \u30AF\u30A8\u30EA\u3092\u51E6\u7406\n    for v in tp_order[::-1]:\n        for\
    \ chi_v in di_tree[v]:\n            if keeps[chi_v] == 0:\n                calc(chi_v,\
    \ 1)\n        add(v)\n        # \u3053\u3053\u3067\u30AF\u30A8\u30EA\u3092\u5B9F\
    \u884C\u3059\u308B\n        query(v)\n        if keeps[v] == 0:\n            calc(v,\
    \ 0)\n"
  dependsOn:
  - Graph/Tree/topological_sorted.py
  isVerificationFile: false
  path: Graph/Tree/dsu_on_tree.py
  requiredBy: []
  timestamp: '2021-07-24 16:52:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/vertex_add_subtree_sum.dsu_on_tree.test.py
documentation_of: Graph/Tree/dsu_on_tree.py
layout: document
title: DSU on tree
---

## 参考
- [[Tutorial] Sack (dsu on tree) - Codeforces](https://codeforces.com/blog/entry/44351)
- [DSU on Tree - Speaker Deck](https://speakerdeck.com/camypaper/dsu-on-tree)