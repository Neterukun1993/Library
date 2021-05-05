from Graph.Tree.centroid import centroid
from Graph.Tree.topological_sorted import topological_sorted


MAX = 0
HASHMAP = {}


def treehash(tree, root=None):
    global MAX
    n = len(tree)
    if root is None:
        hs = centroid(tree)
    else:
        hs = [root]
    res = []
    for rt in hs:
        tp_order, _ = topological_sorted(tree, rt)
        visited = [-1] * n
        for v in tp_order[::-1]:
            tmp = []
            for nxt_v in tree[v]:
                if visited[nxt_v] == -1:
                    continue
                else:
                    tmp.append(visited[nxt_v])
            tmp = tuple(sorted(tmp))
            if tmp not in HASHMAP:
                HASHMAP[tmp] = MAX
                MAX += 1
            visited[v] = HASHMAP[tmp]
        res.append(visited[rt])
    res = tuple(sorted(res))
    return res
