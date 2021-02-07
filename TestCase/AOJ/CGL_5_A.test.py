# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_5_A
import sys
input = sys.stdin.buffer.readline

from Geometry.closest_pair import closest_pair


def main():
    n = int(input())
    points = [list(map(float, input().split())) for i in range(n)]

    print('{:.10f}'.format(closest_pair(points)))


if __name__ == '__main__':
    main()
