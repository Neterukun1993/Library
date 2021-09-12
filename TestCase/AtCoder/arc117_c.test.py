# verification-helper: PROBLEM https://atcoder.jp/contests/arc117/tasks/arc117_c
import sys
input = sys.stdin.readline

from Combination.LucasTheorem import LucasTheorem


def main():
    value = {"B": 0, "W": 1, "R": 2}
    ans = ["B", "W", "R"]
    n = int(input())
    s = input()[:-1]

    lt = LucasTheorem(3)
    res = 0
    for i, si in enumerate(s):
        res += lt.comb(n - 1, i) * value[si]
        res %= 3

    if n % 2 == 0:
        res = (-res) % 3

    print(ans[res])


if __name__ == '__main__':
    main()
