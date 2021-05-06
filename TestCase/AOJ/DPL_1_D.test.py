# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D
import sys
input = sys.stdin.readline

from DP.lis import lis


def main():
    n = int(input())
    a = [int(input()) for i in range(n)]

    ans = len(lis(a))
    print(ans)


if __name__ == '__main__':
    main()
