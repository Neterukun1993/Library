# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
import sys
input = sys.stdin.readline

from Graph.SpanningTree.kruskal import kruskal


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    print(kruskal(n, edges))


if __name__ == '__main__':
    main()
