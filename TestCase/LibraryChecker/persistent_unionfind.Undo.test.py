# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind
import sys
from collections import defaultdict
input = sys.stdin.buffer.readline

from DataStructure.UnionFind.UnionFindUndo import UnionFindUndo


def main():
    """クエリ先読みによって、merge時に参照/生成されるグラフ間に辺を貼り、
    木を構築する。その後オフラインダイコネと同様の要領でシミュレートする。
    """
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(q)]
    judges = defaultdict(list)
    merges = {}
    for i, (flag, k, u, v) in enumerate(queries):
        if k == -1:
            k = q - 1
        if flag == 0:
            if i == q - 1:
                continue
            tree[i].append(k)
            tree[k].append(i)
            merges[i] = (u, v)
        else:
            judges[k].append((i, u, v))

    root = q - 1
    visited = [False] * q
    visited[root] = True
    idxs = [0] * q
    stack = [root]

    # TODO: 木上の巡回をオイラーツアーとしてライブラリにする
    order = []
    while True:
        v = stack.pop()
        idx = idxs[v]
        if idx == len(tree[v]):
            break
        if idx == 0:
            order.append(v)
        if visited[tree[v][idx]] and idx == len(tree[v]) - 1:
            order.append(v)
            stack.append(tree[v][idx])
            tree[v][idx] += 1
            continue
        if visited[tree[v][idx]]:
            tree[v][idx], tree[v][idx + 1] = tree[v][idx + 1], tree[v][idx]
        visited[tree[v][idx]] = True
        stack.append(tree[v][idx])
        idxs[v] += 1

    ans = [-1] * q
    visited = [False] * q
    uf = UnionFindUndo(n)
    for i in order:
        if i in merges:
            if visited[i]:
                uf.undo()
                continue
            else:
                visited[i] = True
                uf.merge(*merges[i])
        for j, u, v in judges[i]:
            ans[j] = int(uf.same(u, v))

    print('\n'.join(map(str, [res for res in ans if res != -1])))


if __name__ == '__main__':
    main()
