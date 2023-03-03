# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence
import sys
input = sys.stdin.buffer.readline


from DP.lis import lis_index


def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = lis_index(a, strict=True)

    print(len(result))
    print(*result)


if __name__ == '__main__':
    main()
