# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    bit = BinaryIndexedTree(n)
    ans = []
    for flag, x, y in queries:
        if flag == 0:
            i = x - 1
            bit.add(i, y)
        else:
            l, r = x - 1, y
            ans.append(bit.sum(l, r))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
