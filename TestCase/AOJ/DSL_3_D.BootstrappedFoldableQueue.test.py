# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.BootstrappedFoldableQueue import BootstrappedFoldableQueue


def main():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    bfq = BootstrappedFoldableQueue(min)
    for i in range(l - 1):
        bfq = bfq.snoc(a[i])

    ans = []
    for i in range(l - 1, n):
        bfq = bfq.snoc(a[i])
        ans.append(bfq.all_fold())
        bfq = bfq.tail()

    print(*ans)


if __name__ == '__main__':
    main()
