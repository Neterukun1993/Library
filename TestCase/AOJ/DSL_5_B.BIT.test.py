# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.RangeAddPointGet2D import BinaryIndexedTree


def main():
    n = int(input())
    queries = [list(map(int, input().split())) for i in range(n)]

    bit = BinaryIndexedTree(1000, 1000)
    for hl, wl, hr, wr in queries:
        bit.add(hl, hr, wl, wr, 1)

    ans = 0
    for i in range(1000):
        for j in range(1000):
            ans = max(ans, bit[i, j])
    print(ans)


if __name__ == '__main__':
    main()
