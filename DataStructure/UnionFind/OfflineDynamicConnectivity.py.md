---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/UnionFindUndo.py
    title: "\u5DFB\u304D\u623B\u3057\u53EF\u80FD Union Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/2235.test.py
    title: TestCase/AOJ/2235.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.UnionFind.UnionFindUndo import UnionFindUndo\n\n\nclass\
    \ OfflineDynamicConnectivity:\n    def __init__(self, q, questions, n):\n    \
    \    self.q = q\n        self.questions = questions\n        self.n = n\n    \
    \    self.add_time = {}\n        self.exist = {}\n        self.pend = []\n\n \
    \       self.size = 2 ** ((q - 1).bit_length())\n        self.node = [[] for _\
    \ in range(2 * self.size)]\n        self.uf = UnionFindUndo(n)\n\n    def insert(self,\
    \ t, u, v):\n        \"\"\"insert (u, v) edge at time t\"\"\"\n        if u >\
    \ v:\n            u, v = v, u\n        uv = u * self.n + v\n        self.add_time[uv]\
    \ = t\n        self.exist[uv] = True\n\n    def erase(self, t, u, v):\n      \
    \  \"\"\"erase (u, v) edge at time t\"\"\"\n        if u > v:\n            u,\
    \ v = v, u\n        uv = u * self.n + v\n        self.exist[uv] = False\n    \
    \    self.pend.append((self.add_time[uv], t, uv))\n\n    def construct(self):\n\
    \        \"\"\"construct query on Segment Tree\"\"\"\n        for uv in self.exist:\n\
    \            if self.exist[uv]:\n                self.pend.append((self.add_time[uv],\
    \ self.q, uv))\n        for l, r, uv in self.pend:\n            self._add(l, r,\
    \ uv)\n\n    def run(self):\n        \"\"\"run queries and get results\"\"\"\n\
    \        self.res = []\n        self._dfs()\n        return self.res\n\n    def\
    \ _add(self, l, r, uv):\n        \"\"\"add (u, v) edge in [l, r) of Segment Tree\"\
    \"\"\n        l, r = l + self.size, r + self.size\n        while l < r:\n    \
    \        if l & 1:\n                self.node[l].append(uv)\n                l\
    \ += 1\n            if r & 1:\n                r -= 1\n                self.node[r].append(uv)\n\
    \            l, r = l >> 1, r >> 1\n\n    def _dfs(self, k=1):\n        \"\"\"\
    DFS on Segment Tree\"\"\"\n        if k >= self.size + self.q:\n            return\n\
    \        for uv in self.node[k]:  # pre-process\n            u, v = divmod(uv,\
    \ self.n)\n            self.uf.merge(u, v)\n\n        if k >= self.size:\n   \
    \         self.res.append(self.uf.same(*self.questions[k - self.size]))\n    \
    \    else:\n            self._dfs(2 * k)\n            self._dfs(2 * k + 1)\n\n\
    \        for _ in range(len(self.node[k])):  # post-process\n            self.uf.undo()\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFindUndo.py
  isVerificationFile: false
  path: DataStructure/UnionFind/OfflineDynamicConnectivity.py
  requiredBy: []
  timestamp: '2021-01-04 02:54:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/2235.test.py
documentation_of: DataStructure/UnionFind/OfflineDynamicConnectivity.py
layout: document
title: Offline Dynamic Connectivity
---

## 概要
無向グラフに対して、辺の追加や削除がある場合の連結判定をオフラインで実行する。

## 使い方
`OfflineDynamicConnectivity(q: int, questions: Sequence[Tuple[int, int, int]], n: int)`  
$n$ 頂点の辺のない無向グラフを初期構築する。予め $q$ 個のクエリを与えておく。計算量 $O(n + q)$  
$i$ 番目のクエリ `questions[i]` の意味は次の通りである。
```
t u v
```
時刻 $t$ のとき、頂点 $u$ と頂点 $v$ は連結か？

- `insert(t: int, u: int, v: int) -> None`  
時刻 $t$ において、頂点 $u$ と頂点 $v$ に辺を張るという操作を与える。**時刻 $t$ は、最後に `insert` や `merge` を行ったときの時刻 $t_{\mathrm{last}}$ よりも大きくすること！** 計算量 $O(1)$

- `erase(t: int, u: int, v: int) -> None`  
時刻 $t$ において、頂点 $u$ と頂点 $v$ の辺を削除するという操作を与える。**時刻 $t$ は、最後に `insert` や `merge` を行ったときの時刻 $t_{\mathrm{last}}$ よりも大きくすること！** 計算量 $O(1)$

- `construct() -> int`  
与えられた `insert` と `erase` の操作をセグメント木上に構築する。`insert` と `erase` を行った回数を $r$ 回とすると、計算量 $O(r \log q)$

- `run() -> List[bool]`  
`construct` したクエリを実行し、その結果を返す。計算量 $O(q + r\log q\log n)$
