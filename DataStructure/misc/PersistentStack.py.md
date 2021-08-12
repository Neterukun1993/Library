---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PersistentStack:\n    def __init__(self, val=None, prev=None):\n  \
    \      self.val = val\n        self.prev = prev\n\n    def top(self):\n      \
    \  return self.val\n\n    def push(self, x):\n        return PersistentStack(x,\
    \ self)\n\n    def pop(self):\n        return self.prev\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/PersistentStack.py
  requiredBy: []
  timestamp: '2021-02-02 21:07:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/misc/PersistentStack.py
layout: document
title: "\u6C38\u7D9AStack"
---

## 概要
Stack を永続化したデータ構造。一応、経路復元などに使える。

## 使い方
`PersistentStack(val=None, prev=None)`  
空の Persistent Stack を構築する。計算量 $O(1)$

- `top() -> Any`  
Persistent Stack の末尾の要素を返す。計算量 $O(1)$

- `push(val: Any) -> PersistentStack`  
末尾に要素 `val` を追加した Persistent Stack を返す。計算量 $O(1)$

- `pop() -> PersistentStack`  
末尾の要素を削除した Persistent Stack を返す。計算量 $O(1)$`