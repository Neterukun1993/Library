# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_A
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
    for v in sorted(ll.enumerate_articulations()):
        print(v)


if __name__ == '__main__':
    main()
