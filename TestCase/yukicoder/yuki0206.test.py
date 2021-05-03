# verification-helper: PROBLEM https://yukicoder.me/problems/no/206
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.fft_convolve import fft_convolve


def main():
    l, m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())

    cnta = [0] * (n + 1)
    cntb = [0] * (n + 1)
    for val in a:
        cnta[val] += 1
    for val in b:
        cntb[n - val] += 1

    conv = fft_convolve(cnta, cntb)

    for i in range(n, n + q):
        print(conv[i])


if __name__ == '__main__':
    main()
