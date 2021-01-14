# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst
import sys
input = sys.stdin.buffer.readline

from Graph.SpanningTree.directed_mst import directed_mst


def main():
    n, m, root = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    res, par = directed_mst(n, edges, root)
    if res == -1:
        print(res)
    else:
        print(res)
        print(*[p if p != -1 else i for i, p in enumerate(par)])


if __name__ == '__main__':
    main()
