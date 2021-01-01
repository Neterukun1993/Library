# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
import sys
input = sys.stdin.buffer.readline

from Library.DataStructure.AccumulateSum.AccumulateSum import AccumulateSum


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]

    acc = AccumulateSum(a)
    ans = []
    for l, r in queries:
        ans.append(acc.sum(l, r))
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
