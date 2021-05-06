# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument
import sys
input = sys.stdin.buffer.readline

from Geometry.atan2_sorted import atan2_sorted


def main():
    n = int(input())
    coords = [list(map(int, input().split())) for i in range(n)]

    ans = atan2_sorted(coords)
    for res in ans:
        print(*res)


if __name__ == '__main__':
    main()
