# verification-helper: PROBLEM https://judge.yosupo.jp/problem/segment_add_get_min
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.LiChaoTree import LiChaoTree


def main():
    n, q = map(int, input().split())
    segs = [list(map(int, input().split())) for i in range(n)]
    queries = [list(map(int, input().split())) for i in range(q)]
    INF = 10 ** 18

    xs = []
    for flag, *query in queries:
        if flag:
            xs.append(query[0])

    lct = LiChaoTree(xs)
    for l, r, a, b in segs:
        line = (a, b)
        lct.add_seg(line, l, r)

    ans = []
    for flag, *query in queries:
        if flag == 0:
            l, r, a, b = query
            line = (a, b)
            lct.add_seg(line, l, r)
        else:
            p = query[0]
            res = lct.min(p)
            if res == INF:
                ans.append("INFINITY")
            else:
                ans.append(str(res))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
