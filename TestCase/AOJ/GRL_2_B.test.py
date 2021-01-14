# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_B
import sys
input = sys.stdin.buffer.readline

from Graph.SpanningTree.directed_mst import directed_mst


def main():
    n, m, root = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    res, par = directed_mst(n, edges, root)
    print(res)


if __name__ == '__main__':
    main()
