# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C
from DP.lcs import lcs


def main():
    q = int(input())
    for _ in range(q):
        x = input()
        y = input()

        print(len(lcs(x, y)))


if __name__ == '__main__':
    main()
