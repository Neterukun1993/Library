# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_C
import sys
input = sys.stdin.buffer.readline

from DP.largest_rectangle_in_histogram import largest_rectangle_in_histogram


def main():
    n = int(input())
    h = list(map(int, input().split()))

    ans = largest_rectangle_in_histogram(h)
    print(ans)


if __name__ == '__main__':
    main()
