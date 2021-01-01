# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.DualSegmentTree import DualSegmentTree


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    unitA = (False, (1 << 31) - 1)
    A_f = lambda a1, a2: a2 if a2[0] else a1
    dst = DualSegmentTree(n, unitA, A_f)
    ans = []
    for flag, *query in queries:
        if flag == 0:
            l, r, x = query
            r += 1
            dst.range_apply(l, r, (True, x))
        else:
            i = query[0]
            ans.append(dst[i][1])

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
