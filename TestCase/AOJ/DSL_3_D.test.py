# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.SlidingWindowAggregation import SlidingWindowAggregation


def main():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    swag = SlidingWindowAggregation(min)
    for i in range(l - 1):
        swag.append(a[i])

    ans = []
    for i in range(l - 1, n):
        swag.append(a[i])
        ans.append(swag.all_fold())
        swag.popleft()

    print(*ans)


if __name__ == '__main__':
    main()
