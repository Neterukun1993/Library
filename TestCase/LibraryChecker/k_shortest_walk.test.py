# verification-helper: PROBLEM https://judge.yosupo.jp/problem/k_shortest_walk
import sys
input = sys.stdin.buffer.readline

from Graph.misc.k_shortest_walk import k_shortest_walk


def main():
    n, m, start, goal, k = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    ans = k_shortest_walk(n, edges, start, goal, k)
    for res in ans:
        print(res)


if __name__ == '__main__':
    main()
