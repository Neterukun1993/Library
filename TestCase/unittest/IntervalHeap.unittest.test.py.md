---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Heap/IntervalHeap.py
    title: Interval Heap
  - icon: ':heavy_check_mark:'
    path: misc/xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.Heap.IntervalHeap\
    \ import IntervalHeap\nfrom misc.xorshift import xorshift32\n\n\ndef main():\n\
    \    # \u6607\u9806push / \u6607\u9806pop\n    ih = IntervalHeap()\n    for i\
    \ in range(100):\n        ih.push(i)\n        assert(ih.max == i)\n        assert(ih.min\
    \ == 0)\n    for i in range(100):\n        val = ih.min\n        poped = ih.pop_min()\n\
    \        assert(val == poped)\n\n    # \u6607\u9806push / \u964D\u9806pop\n  \
    \  ih = IntervalHeap()\n    for i in range(100):\n        ih.push(i)\n       \
    \ assert(ih.max == i)\n        assert(ih.min == 0)\n    for i in range(100):\n\
    \        val = ih.max\n        poped = ih.pop_max()\n        assert(val == poped)\n\
    \n    # \u964D\u9806push / \u6607\u9806pop\n    ih = IntervalHeap()\n    for i\
    \ in reversed(range(100)):\n        ih.push(i)\n        assert(ih.max == 99)\n\
    \        assert(ih.min == i)\n    for i in range(100):\n        val = ih.min\n\
    \        poped = ih.pop_min()\n        assert(val == poped)\n\n    # \u964D\u9806\
    push / \u964D\u9806pop\n    ih = IntervalHeap()\n    for i in reversed(range(100)):\n\
    \        ih.push(i)\n        assert(ih.max == 99)\n        assert(ih.min == i)\n\
    \    for i in range(100):\n        val = ih.max\n        poped = ih.pop_max()\n\
    \        assert(val == poped)\n\n    # \u30E9\u30F3\u30C0\u30E0\n    ih = IntervalHeap()\n\
    \    rand32 = xorshift32()\n    array = []\n    for i in range(100):\n       \
    \ val = rand32()\n        ih.push(val)\n        array.append(val)\n        assert(ih.max\
    \ == max(array))\n        assert(ih.min == min(array))\n\n    for i in range(1000):\n\
    \        val = ih.min\n        poped = ih.pop_min()\n        assert(val == poped)\n\
    \        assert(val == min(array))\n        del array[array.index(val)]\n\n  \
    \      val = ih.max\n        poped = ih.pop_max()\n        assert(val == poped)\n\
    \        assert(val == max(array))\n        del array[array.index(val)]\n\n  \
    \      for _ in range(2):\n            val = rand32()\n            ih.push(val)\n\
    \            array.append(val)\n\n\nif __name__ == '__main__':\n    main()\n \
    \   print(\"Hello World\")\n"
  dependsOn:
  - misc/xorshift.py
  - DataStructure/Heap/IntervalHeap.py
  isVerificationFile: true
  path: TestCase/unittest/IntervalHeap.unittest.test.py
  requiredBy: []
  timestamp: '2021-05-08 17:40:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/IntervalHeap.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/IntervalHeap.unittest.test.py
- /verify/TestCase/unittest/IntervalHeap.unittest.test.py.html
title: TestCase/unittest/IntervalHeap.unittest.test.py
---
