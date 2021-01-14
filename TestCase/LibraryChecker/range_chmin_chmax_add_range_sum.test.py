# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.SegmentTreeBeats import SegmentTreeBeats


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for i in range(q)]

    stb = SegmentTreeBeats(n)
    stb.build(a)

    ans = []
    for flag, *query in queries:
        if flag == 0:
            l, r, b = query
            stb.range_chmin(l, r, b)
        elif flag == 1:
            l, r, b = query
            stb.range_chmax(l, r, b)
        elif flag == 2:
            l, r, b = query
            stb.range_add(l, r, b)
        else:
            l, r = query
            ans.append(stb.fold_sum(l, r))

    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
