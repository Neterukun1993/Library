# verification-helper: PROBLEM https://yukicoder.me/problems/no/3030
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Prime.miller_rabin import miller_rabin


def main():
    n = int(input())
    x = [int(input()) for i in range(n)]

    for val in x:
        print(val, int(miller_rabin(val)))


if __name__ == '__main__':
    main()
