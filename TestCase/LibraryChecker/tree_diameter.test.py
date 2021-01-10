# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.diameter import diameter


def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]

    tree = [[] for i in range(n)]
    for a, b, cost in edges:
        tree[a].append((b, cost))
        tree[b].append((a, cost))

    diam, path = diameter(tree)
    print(diam, len(path))
    print(*path)


if __name__ == '__main__':
    main()
