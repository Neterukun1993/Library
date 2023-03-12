# verification-helper: PROBLEM https://atcoder.jp/contests/abc242/tasks/abc242_g
import sys
input = sys.stdin.buffer.readline

from misc.mo_algorithm import mo_algorithm


def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    cnt = [0]
    count = [0] * (n + 1)

    def add(x):
        cnt[0] += count[a[x]]
        count[a[x]] ^= 1

    def rem(x):
        count[a[x]] ^= 1
        cnt[0] -= count[a[x]]

    def get():
        return cnt[0]

    ans = mo_algorithm(
        n, q, [(l - 1, r) for l, r in queries],
        add, add, rem, rem, get
    )

    for res in ans:
        print(res)


if __name__ == '__main__':
    main()
