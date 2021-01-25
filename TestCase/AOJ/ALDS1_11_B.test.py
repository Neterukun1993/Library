# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B
import sys
input = sys.stdin.buffer.readline

from Graph.misc.DigraphDFSTree import DigraphDFSTree


def main():
    n = int(input())
    info = [list(map(int, input().split())) for i in range(n)]

    dfst = DigraphDFSTree(n)
    for v, k, *nxt_vs in info:
        v -= 1
        for nxt_v in nxt_vs:
            nxt_v -= 1
            dfst.add_edge(v, nxt_v)

    dfst.build()
    for i, (arr, dep) in enumerate(zip(dfst.arrival, dfst.depature)):
        print(i + 1, arr + 1, dep + 1)


if __name__ == '__main__':
    main()
