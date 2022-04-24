---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_1_C.SplayTree.test.py
    title: TestCase/AOJ/ITP2_1_C.SplayTree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class STNode:\n    def __init__(self, val):\n        self.val = val\n   \
    \     self.l, self.r, self.p = None, None, None\n        self.size = 1\n\n   \
    \ def update(self):\n        self.size = 1\n        if self.l is not None: self.size\
    \ += self.l.size\n        if self.r is not None: self.size += self.r.size\n\n\
    \    def state(self):\n        if self.p is None: return 0\n        if self.p.l\
    \ == self: return 1\n        else: return -1  # self.p.r == self\n\n    def splay(self):\n\
    \        while self.p is not None:\n            st, st_p = self.state(), self.p.state()\n\
    \            if st_p == 0:\n                if st == 1: self.p._rotr()\n     \
    \           else: self.p._rotl()\n            elif st_p == 1:\n              \
    \  if st == 1:\n                    self.p.p._rotr()\n                    self.p._rotr()\n\
    \                else:\n                    self.p._rotl()\n                 \
    \   self.p._rotr()\n            else:\n                if st == 1:\n         \
    \           self.p._rotr()\n                    self.p._rotl()\n             \
    \   else:\n                    self.p.p._rotl()\n                    self.p._rotl()\n\
    \        return self\n\n    def _rotl(self):\n        nd = self.r\n        nd.p\
    \ = self.p\n        if nd.p is not None:\n            if nd.p.l is self: nd.p.l\
    \ = nd\n            else: nd.p.r = nd\n        self.r = nd.l\n        if self.r\
    \ is not None: self.r.p = self\n        self.p = nd\n        nd.l = self\n   \
    \     self.update()\n        nd.update()\n\n    def _rotr(self):\n        nd =\
    \ self.l\n        nd.p = self.p\n        if nd.p is not None:\n            if\
    \ nd.p.r is self: nd.p.r = nd\n            else: nd.p.l = nd\n        self.l =\
    \ nd.r\n        if self.l is not None: self.l.p = self\n        self.p = nd\n\
    \        nd.r = self\n        self.update()\n        nd.update()\n\n\nclass SplayTreeList:\n\
    \    def __init__(self):\n        self.root = None\n\n    def __getitem__(self,\
    \ idx):\n        self._splay(idx)\n        return self.root.val\n\n    def __setitem__(self,\
    \ idx, val):\n        self._splay(idx)\n        self.root.val = val\n\n    def\
    \ __len__(self):\n        return self.root.size if self.root is not None else\
    \ 0\n\n    def _splay(self, idx):\n        nd = self.root\n        while True:\n\
    \            sizel = nd.l.size if nd.l is not None else 0\n            if idx\
    \ < sizel: nd = nd.l\n            elif idx > sizel:\n                nd = nd.r\n\
    \                idx -= sizel + 1\n            else:\n                self.root\
    \ = nd.splay()\n                break\n\n    def _merge(self, rtl, rtr):\n   \
    \     if rtl is None: return rtr\n        if rtr is None: return rtl\n       \
    \ while rtl.r is not None:\n            rtl = rtl.r\n        rtl = rtl.splay()\n\
    \        rtl.r = rtr\n        rtr.p = rtl\n        rtl.update()\n        return\
    \ rtl\n\n    def _split(self, cntl):\n        if cntl == 0: return None, self.root\n\
    \        if cntl == self.root.size: return self.root, None\n        self._splay(cntl)\n\
    \        rtl = self.root.l\n        rtr = self.root\n        rtl.p = None\n  \
    \      rtr.l = None\n        rtr.update()\n        return rtl, rtr\n\n    def\
    \ insert(self, idx, val):\n        rtl, rtr = self._split(idx)\n        rt = STNode(val)\n\
    \        self.root = self._merge(self._merge(rtl, rt), rtr)\n\n    def delete(self,\
    \ idx):\n        self._splay(idx)\n        rtl = self.root.l\n        rtr = self.root.r\n\
    \        if rtl is not None: rtl.p = None\n        if rtr is not None: rtr.p =\
    \ None\n        self.root = self._merge(rtl, rtr)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/List/SplayTreeList.py
  requiredBy: []
  timestamp: '2022-01-23 04:17:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_1_C.SplayTree.test.py
documentation_of: DataStructure/List/SplayTreeList.py
layout: document
title: "\u5BFE\u6570\u6642\u9593\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9/\u633F\
  \u5165/\u524A\u9664\u53EF\u80FD\u30EA\u30B9\u30C8 (\u30B9\u30D7\u30EC\u30FC\u6728\
  )"
---
