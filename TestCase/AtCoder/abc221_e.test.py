# verification-helper: PROBLEM https://atcoder.jp/contests/abc221/tasks/abc221_e

import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.RSQ_RMultipleQ import RSQ_RMultipleQ


def main():
    MOD = 998244353
    n = int(input())
    a = list(map(int, input().split()))

    mapping = {val: i for i, val in enumerate(sorted(set(a)))}
    m = len(mapping)
    st = RSQ_RMultipleQ(m)

    ans = 0
    for val in a:
        idx = mapping[val]
        ans += st.fold(0, idx + 1)
        ans %= MOD

        st.range_apply(0, m, 2)
        st[idx] = st[idx] + 1

    print(ans)


if __name__ == '__main__':
    main()
