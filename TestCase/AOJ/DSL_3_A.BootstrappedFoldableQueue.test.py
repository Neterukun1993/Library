# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.BootstrappedFoldableQueue import BootstrappedFoldableQueue


def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    bfq = BootstrappedFoldableQueue(lambda x, y: x + y)
    ans = 10 ** 18
    r = 0
    for l in range(n):
        if not bfq:
            bfq = bfq.snoc(a[r])
            r += 1
        while r < n and bfq.all_fold() < s:
            bfq = bfq.snoc(a[r])
            r += 1
        if bfq.all_fold() >= s:
            ans = min(r - l, ans)
        bfq = bfq.tail()

    if ans == 10 ** 18:
        print(0)
    else:
        print(ans)


if __name__ == '__main__':
    main()
