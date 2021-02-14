# verification-helper: PROBLEM https://yukicoder.me/problems/no/763
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.topological_sorted import topological_sorted


def main():
    n = int(input())
    edges = [list(map(int, input().split())) for i in range(n - 1)]

    tree = [[] for i in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)

    tp_order, par = topological_sorted(tree, 0)
    dp0 = [0] * n
    dp1 = [0] * n

    for v in tp_order[::-1]:
        for nxt_v in tree[v]:
            if nxt_v == par[v]:
                continue
            dp0[v] += max(dp0[nxt_v], dp1[nxt_v])
            dp1[v] += max(dp0[nxt_v], dp1[nxt_v] - 1)
        dp1[v] += 1

    print(max(max(dp0), max(dp1)))


if __name__ == '__main__':
    main()
