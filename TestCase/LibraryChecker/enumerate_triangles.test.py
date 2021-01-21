# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_triangles
import sys
input = sys.stdin.buffer.readline

from Graph.misc.enumerate_triangles import enumerate_triangles


def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for i in range(m)]
    MOD = 998244353

    _, ans = enumerate_triangles(edges, x, MOD)
    print(ans)


if __name__ == '__main__':
    main()
