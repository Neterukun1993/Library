# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_5_A
import sys
input = sys.stdin.buffer.readline

from Geometry.closest_pair import closest_pair


def main():
    n = int(input())
    points = [list(map(float, input().split())) for i in range(n)]

    points.sort()
    print('{:.012f}'.format(closest_pair(points)[0]))


if __name__ == '__main__':
    main()
