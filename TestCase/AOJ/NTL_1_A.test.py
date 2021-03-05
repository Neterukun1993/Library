# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Prime.prime_factors import prime_factors, prime_factors_distinct, prime_factors_compress


def main():
    n = int(input())

    pf = prime_factors(n)
    pf_distinct = prime_factors_distinct(n)
    pf_compress = prime_factors_compress(n)

    assert(sorted(set(pf)) == pf_distinct)
    pf_test = []
    for val, cnt in pf_compress:
        for _ in range(cnt):
            pf_test.append(val)
    assert(pf_test == pf)

    print(f'{n}: {" ".join(map(str, pf))}')


if __name__ == '__main__':
    main()
