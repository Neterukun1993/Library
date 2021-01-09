# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B
import sys
input = sys.stdin.readline

from Graph.LowLink import LowLink


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    ll = LowLink(n)
    for u, v in edges:
        ll.add_edge(u, v)

    ll.build()
    bs = [(u, v) if u < v else (v, u) for u, v in ll.enumerate_bridges()]
    for u, v in sorted(bs):
        print(u, v)


if __name__ == '__main__':
    main()
