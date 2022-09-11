# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.FoldableQueue import FoldableQueue


def main():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    fq = FoldableQueue(min)
    for i in range(l - 1):
        fq.append(a[i])

    ans = []
    for i in range(l - 1, n):
        fq.append(a[i])
        ans.append(fq.all_fold())
        fq.popleft()

    print(*ans)


if __name__ == '__main__':
    main()
