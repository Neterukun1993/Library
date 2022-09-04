---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/DoublingLCA.py
    title: "\u6700\u5C0F\u5171\u901A\u7956\u5148 (\u30C0\u30D6\u30EA\u30F3\u30B0)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/jump_on_tree
    links:
    - https://judge.yosupo.jp/problem/jump_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Tree.DoublingLCA import\
    \ DoublingLCA\n\n\ndef main():\n    n, q = map(int, input().split())\n    edges\
    \ = [list(map(int, input().split())) for i in range(n - 1)]\n    queries = [list(map(int,\
    \ input().split())) for i in range(q)]\n\n    tree = [[] for i in range(n)]\n\
    \    for u, v in edges:\n        tree[u].append(v)\n        tree[v].append(u)\n\
    \n    db = DoublingLCA(tree, 0)\n    ans = []\n    for u, v, k in queries:\n \
    \       ans.append(db.jump(u, v, k))\n\n    print('\\n'.join(map(str, ans)))\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/DoublingLCA.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/jump_on_tree.Doubling.test.py
  requiredBy: []
  timestamp: '2022-09-04 19:01:08+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/jump_on_tree.Doubling.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/jump_on_tree.Doubling.test.py
- /verify/TestCase/LibraryChecker/jump_on_tree.Doubling.test.py.html
title: TestCase/LibraryChecker/jump_on_tree.Doubling.test.py
---
