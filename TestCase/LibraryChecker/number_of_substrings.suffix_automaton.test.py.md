---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: String/SuffixAutomaton.py
    title: Suffix automaton
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/number_of_substrings
    links:
    - https://judge.yosupo.jp/problem/number_of_substrings
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_substrings\n\
    import sys\ninput = sys.stdin.readline\n\nfrom String.SuffixAutomaton import SuffixAutomaton\n\
    \n\ndef main():\n    s = input().replace('\\n', '')\n\n    sa = SuffixAutomaton()\n\
    \    for char in s:\n        sa.push(char)\n\n    print(sa.number_of_substrings())\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - String/SuffixAutomaton.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/number_of_substrings.suffix_automaton.test.py
  requiredBy: []
  timestamp: '2021-06-13 17:43:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/number_of_substrings.suffix_automaton.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/number_of_substrings.suffix_automaton.test.py
- /verify/TestCase/LibraryChecker/number_of_substrings.suffix_automaton.test.py.html
title: TestCase/LibraryChecker/number_of_substrings.suffix_automaton.test.py
---
