# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A
import sys
input = sys.stdin.buffer.readline

from Geometry.convexhull import convexhull


def main():
    n = int(input())
    points = [list(map(int, input().split())) for i in range(n)]

    ch = convexhull(points)
    x, y = 10 ** 8, 10 ** 8
    minidx = 0
    for i in range(len(ch)):
        if ch[i][1] < y or (ch[i][1] == y and ch[i][0] < x):
            minidx = i
            x, y = ch[i]
    ch = ch[minidx:] + ch[:minidx]

    print(len(ch))
    for res in ch:
        print(*res)


if __name__ == '__main__':
    main()
