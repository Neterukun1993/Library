# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Prime.divisors import divisors


def main():
    a, b, c = map(int, input().split())

    divs = divisors(c)
    ans = 0
    for val in divs:
        ans += (a <= val <= b)

    print(ans)

if __name__ == '__main__':
    main()
