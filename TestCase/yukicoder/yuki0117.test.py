# verification-helper: PROBLEM https://yukicoder.me/problems/no/117
import re

from Combination.modinv_combination import Combination


def main():
    t = int(input())
    queries = [re.split('[(,)]', input()) for i in range(t)]

    MOD = 10 ** 9 + 7
    comb = Combination(2 * 10 ** 6 + 10, MOD)
    ans = []
    for char, n, r, _ in queries:
        n = int(n)
        r = int(r)
        if char == "P":
            ans.append(comb.perm(n, r))
        elif char == "C":
            ans.append(comb.comb(n, r))
        else:
            if n == r and n == 0:
                ans.append(1)
            else:
                ans.append(comb.comb(n + r - 1, r))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
