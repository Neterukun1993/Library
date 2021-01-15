# verification-helper: PROBLEM https://yukicoder.me/problems/no/117
import sys
input = sys.stdin.readline

from Combination.modinv_combination import Combination


def main():
    t = int(input())
    queries = []
    for _ in range(t):
        string = input().replace('\n', '')
        tmp = []
        s = ''
        for i in string:
            if i in ('(,)'):
                tmp.append(s)
                s = ''
            else:
                s += i
        queries.append(tmp)

    MOD = 10 ** 9 + 7
    comb = Combination(2 * 10 ** 6 + 10, MOD)

    for char, n, r in queries:
        n = int(n)
        r = int(r)
        if char == "P":
            print(comb.perm(n, r))
        elif char == "C":
            print(comb.comb(n, r))
        else:
            if n == r and n == 0:
                print(1)
            else:
                print(comb.comb(n + r - 1, r))


if __name__ == '__main__':
    main()
