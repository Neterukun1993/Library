# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum
import sys
input = sys.stdin.buffer.readline

from DataStructure.Wavelet.RectangleSum import CompressedRectangleSum


def main():
    n, q = map(int, input().split())
    points = [list(map(int, input().split())) for i in range(n)]
    queries = [list(map(int, input().split())) for i in range(q)]

    crs = CompressedRectangleSum(points)

    ans = []
    for l, lower, r, upper in queries:
        ans.append(crs.rect_sum(l, r, lower, upper))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
