# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.DoublingLCA import DoublingLCA


def main():
    n, q = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(n - 1)]
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    db = DoublingLCA(tree, 0)
    ans = []
    for u, v, k in queries:
        ans.append(db.jump(u, v, k))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
