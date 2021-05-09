# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from DP.substring_dp import substring_dp
from itertools import product


def bruteforce(small_characters, MOD):
    n = len(small_characters)
    strs = set()

    for bit_state in range(1 << n):
        tmp = ""
        for i in range(n):
            if (bit_state >> i) & 1:
                tmp += small_characters[i]
        strs.add(tmp)
    return len(strs) % MOD


def main():
    ALPH = "abcd"
    MOD = 10 ** 9 + 7

    for rep in range(8):
        for string in product(ALPH, repeat=rep):
            dp_sol = substring_dp(string, MOD)
            bf_sol = bruteforce(string, MOD)
            assert(dp_sol == bf_sol)


if __name__ == '__main__':
    main()
    print("Hello World")
