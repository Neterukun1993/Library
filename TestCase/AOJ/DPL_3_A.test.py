# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_A
import sys
input = sys.stdin.buffer.readline

from DP.largest_square_in_grid import largest_square_in_grid


def main():
    h, w = map(int, input().split())
    c = [list(map(int, input().split())) for i in range(h)]

    ans = largest_square_in_grid(c, wall=1)
    print(ans)


if __name__ == '__main__':
    main()
