# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_G
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.RangeAddRangeSum import BinaryIndexedTree


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    bit = BinaryIndexedTree(n)
    ans = []
    for flag, *query in queries:
        if flag == 0:
            l, r, x = query
            l -= 1
            bit.add(l, r, x)
        else:
            l, r = query
            l -= 1
            ans.append(bit.sum(l, r))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
