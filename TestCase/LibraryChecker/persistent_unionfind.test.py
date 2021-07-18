# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind
import sys
input = sys.stdin.buffer.readline

from DataStructure.UnionFind.PersistentUnionFind import PersistentUnionFind


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    uf = PersistentUnionFind(n)
    states = [None] * (q + 1)
    states[-1] = uf

    ans = []
    for i, (flag, k, u, v) in enumerate(queries):
        if flag == 0:
            states[i] = states[k].merge(u, v)
        else:
            if states[k].same(u, v):
                ans.append(1)
            else:
                ans.append(0)

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
