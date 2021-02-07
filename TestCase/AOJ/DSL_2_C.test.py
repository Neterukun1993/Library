# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.KDTree2D import KDTree2D


def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for i in range(n)]
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    idxs = {}
    for idx, (x, y) in enumerate(points):
        if (x, y) not in idxs:
            idxs[x, y] = []
        idxs[x, y].append(idx)

    kd = KDTree2D(set(points))
    for xl, xr, yl, yr in queries:
        xr += 1
        yr += 1
        res = []
        for x, y in kd.find(xl, xr, yl, yr):
            for idx in idxs[x, y]:
                res.append(idx)
        res.sort()
        if res:
            print('\n'.join(map(str, res)))
            print()
        else:
            print()


if __name__ == '__main__':
    main()
