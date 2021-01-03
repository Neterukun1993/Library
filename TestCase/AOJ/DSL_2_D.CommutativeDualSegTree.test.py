# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.RUQ import RUQ


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    ruq = RUQ(n)
    ruq.range_apply(0, n, (1 << 31) - 1)
    ans = []
    for flag, *query in queries:
        if flag == 0:
            l, r, x = query
            r += 1
            ruq.range_apply(l, r, x)
        else:
            i = query[0]
            ans.append(ruq[i])

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
