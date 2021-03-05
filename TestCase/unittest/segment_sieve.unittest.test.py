# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Prime.segment_sieve import segment_sieve
from NumberTheory.Prime.miller_rabin import miller_rabin


def main():
    length = 10 ** 5
    for l in range(10 ** 9, 10 ** 9 + 10):
        prime_list, prime_table = segment_sieve(l, l + length)
        idx = 0
        for i, is_prime in enumerate(prime_table):
            val = l + i
            assert(is_prime == miller_rabin(val))
            if is_prime:
                assert(prime_list[idx] == val)
                idx += 1


if __name__ == '__main__':
    main()
    print("Hello World")
