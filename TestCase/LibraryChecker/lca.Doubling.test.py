# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.DoublingLCA import DoublingLCA


def main():
    n, q = map(int, input().split())
    p = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    for u, v in enumerate(p):
        u += 1
        tree[u].append(v)
        tree[v].append(u)

    db = DoublingLCA(tree, 0)
    ans = []
    for u, v in queries:
        ans.append(db.lca(u, v))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
