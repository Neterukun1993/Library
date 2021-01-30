# verification-helper: PROBLEM https://yukicoder.me/problems/no/1110
import sys
input = sys.stdin.buffer.readline

from DataStructure.SortedSet.SortedMultiSetBIT import SortedMultiSetBIT


def main():
    # add, count
    n, d = map(int, input().split())
    a = [int(input()) for i in range(n)]

    sset = SortedMultiSetBIT(a)
    for val in a:
        sset.add(val)

    ans = []
    for val in a:
        r = max(val - d + 1, 0)
        ans.append(sset.count(0, r))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
