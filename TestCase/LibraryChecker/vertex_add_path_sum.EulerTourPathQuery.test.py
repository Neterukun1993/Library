# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.EulerTourPathQuery import EulerTourPathQuery


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for i in range(n - 1)]
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    et = EulerTourPathQuery(tree)
    et.build(a)

    ans = []
    for flag, u, v in queries:
        if flag == 0:
            val = v
            et.add(u, val)
        else:
            ans.append(et.vertex_path_sum(u, v))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
