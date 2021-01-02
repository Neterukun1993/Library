# verification-helper: PROBLEM https://judge.yosupo.jp/problem/line_add_get_min
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.LiChaoTree import LiChaoTree


def main():
    n, q = map(int, input().split())
    lines = [list(map(int, input().split())) for i in range(n)]
    queries = [list(map(int, input().split())) for i in range(q)]
    INF = 10 ** 20

    xs = []
    for flag, *query in queries:
        if flag:
            xs.append(query[0])

    lct = LiChaoTree(xs)
    for line in lines:
        lct.add_line(line)

    ans = []
    for flag, *query in queries:
        if flag == 0:
            line = query
            lct.add_line(line)
        else:
            p = query[0]
            ans.append(lct.min(p))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
