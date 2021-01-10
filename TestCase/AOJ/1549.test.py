# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1549
import sys
input = sys.stdin.buffer.readline

from DataStructure.Wavelet.WaveletMatrix import CompressedWaveletMatrix


def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]
    INF = 10 ** 9

    cwm = CompressedWaveletMatrix(a)
    ans = []

    for l, r, k in queries:
        r += 1
        res = INF
        prv = cwm.prev_val(l, r, k)
        nxt = cwm.next_val(l, r, k)
        if prv is not None:
            res = min(res, k - prv)
        if nxt is not None:
            res = min(res, nxt - k)
        ans.append(res)

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
