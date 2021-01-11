# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum
import sys
input = sys.stdin.buffer.readline

from DataStructure.Wavelet.PointAddRectangleSum import CompressedPointAddRectangleSum


def main():
    n, q = map(int, input().split())
    points = [tuple(map(int, input().split())) for i in range(n)]
    queries = [list(map(int, input().split())) for i in range(q)]

    for flag, *query in queries:
        if flag == 0:
            x, y, _ = query
            points.append((x, y, 0))

    crs = CompressedPointAddRectangleSum(points)
    ans = []
    for flag, *query in queries:
        if flag == 0:
            x, y, w = query
            crs.point_add(x, y, w)
        else:
            l, lower, r, upper = query
            ans.append(crs.rect_sum(l, r, lower, upper))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
