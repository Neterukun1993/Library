# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.SlidingWindowAggregation import SlidingWindowAggregation


def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    swag = SlidingWindowAggregation(lambda x, y: x + y)
    ans = 10 ** 18
    r = 0
    for l in range(n):
        if not swag:
            swag.append(a[r])
            r += 1
        while r < n and swag.all_fold() < s:
            swag.append(a[r])
            r += 1
        if swag.all_fold() >= s:
            ans = min(r - l, ans)
        swag.popleft()

    if ans == 10 ** 18:
        print(0)
    else:
        print(ans)


if __name__ == '__main__':
    main()
