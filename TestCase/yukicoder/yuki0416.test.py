# verification-helper: PROBLEM https://yukicoder.me/problems/no/416
import sys
input = sys.stdin.buffer.readline

from DataStructure.UnionFind.PertiallyPersistentUnionFind import PertiallyPersistentUnionFind


def main():
    n, m, q = map(int, input().split())
    edges = [tuple(map(int, input().split())) for i in range(m)]
    queries = [tuple(map(int, input().split())) for i in range(q)]

    remain = set(edges)
    for e in queries:
        remain.remove(e)

    uf = PertiallyPersistentUnionFind(n)
    for a, b in remain:
        a -= 1
        b -= 1
        uf.merge(0, a, b)

    for t, (a, b) in enumerate(queries[::-1]):
        a -= 1
        b -= 1
        t += 1
        uf.merge(t, a, b)

    ans = []
    for v in range(1, n):
        if not uf.same(q, 0, v):
            ans.append(0)
            continue
        ok = q
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if uf.same(mid, 0, v):
                ok = mid
            else:
                ng = mid
        if ok == 0:
            ans.append(-1)
        else:
            ans.append(q - ok + 1)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
