---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/BinaryTrie.py
    title: Binary Trie
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/set_xor_min
    links:
    - https://judge.yosupo.jp/problem/set_xor_min
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/set_xor_min\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.BinaryTrie\
    \ import BinaryTrie\n\n\ndef main():\n    n = int(input())\n    query = [list(map(int,\
    \ input().split())) for i in range(n)]\n\n    bt = BinaryTrie()\n    ans = []\n\
    \    for q, x in query:\n        if q == 0:\n            bt.insert(x)\n      \
    \  elif q == 1:\n            bt.delete(x)\n        else:\n            ans.append(bt.get_xor_min(x))\n\
    \n    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__ == '__main__':\n   \
    \ main()\n"
  dependsOn:
  - DataStructure/misc/BinaryTrie.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/set_xor_min.test.py
  requiredBy: []
  timestamp: '2021-02-05 19:21:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/set_xor_min.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/set_xor_min.test.py
- /verify/TestCase/LibraryChecker/set_xor_min.test.py.html
title: TestCase/LibraryChecker/set_xor_min.test.py
---
