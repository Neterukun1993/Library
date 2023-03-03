---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/BankersQueue.py
    title: "\u6C38\u7D9A Queue (Banker's Queue)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/persistent_queue
    links:
    - https://judge.yosupo.jp/problem/persistent_queue
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_queue\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.BankersQueue\
    \ import BankersQueue\n\n\ndef main():\n    q = int(input())\n    queries = [list(map(int,\
    \ input().split())) for i in range(q)]\n\n    bq = BankersQueue()\n    states\
    \ = [None] * (q + 1)\n    states[-1] = bq\n\n    ans = []\n    for i, (flag, *query)\
    \ in enumerate(queries):\n        if flag == 0:\n            t, x = query\n  \
    \          states[i] = states[t].push(x)\n        else:\n            t = query[0]\n\
    \            ans.append(states[t].front())\n            states[i] = states[t].pop()\n\
    \n    print('\\n'.join(map(str, ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/BankersQueue.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/persistent_queue.test.py
  requiredBy: []
  timestamp: '2021-06-27 18:25:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/persistent_queue.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/persistent_queue.test.py
- /verify/TestCase/LibraryChecker/persistent_queue.test.py.html
title: TestCase/LibraryChecker/persistent_queue.test.py
---
