# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.RMaxQ_RAQ import RMaxQ_RAQ


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    lst = RMaxQ_RAQ(n)
    ans = []
    for flag, *query in queries:
        if flag == 0:
            l, r, x = query
            r += 1
            lst.range_apply(l, r, -x)
        else:
            l, r = query
            r += 1
            ans.append(-lst.fold(l, r))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
