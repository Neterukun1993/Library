# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest
import sys
input = sys.stdin.buffer.readline

from DataStructure.Wavelet.WaveletMatrix import CompressedWaveletMatrix


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for i in range(q)]

    cwm = CompressedWaveletMatrix(a)
    ans = []
    for l, r, k in queries:
        ans.append(cwm.kth_smallest(l, r, k))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
