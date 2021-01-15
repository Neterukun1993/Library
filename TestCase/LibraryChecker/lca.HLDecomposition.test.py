# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.HLDecomposition import HLDecomposition


def main():
    n, q = map(int, input().split())
    p = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    for u, v in enumerate(p):
        u += 1
        tree[u].append(v)
        tree[v].append(u)

    hld = HLDecomposition(tree)
    ans = []
    for u, v in queries:
        ans.append(hld.lca(u, v))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
