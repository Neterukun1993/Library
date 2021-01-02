# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0560
import sys
input = sys.stdin.readline

from DataStructure.BinaryIndexedTree.PointAddRangeSum2D import BinaryIndexedTree


def main():
    m, n = map(int, input().split())
    k = int(input())
    s = [input()[:-1] for i in range(m)]
    queries = [list(map(int, input().split())) for i in range(k)]

    bitJ = BinaryIndexedTree(n, n)
    bitO = BinaryIndexedTree(n, n)
    bitI = BinaryIndexedTree(n, n)

    for i, t in enumerate(s):
        for j, char in enumerate(t):
            if char == "J":
                bitJ.add(i, j, 1)
            elif char == "O":
                bitO.add(i, j, 1)
            else:
                bitI.add(i, j, 1)

    for hl, wl, hr, wr in queries:
        hl -= 1
        wl -= 1
        J = bitJ.sum(hl, hr, wl, wr)
        O = bitO.sum(hl, hr, wl, wr)
        I = bitI.sum(hl, hr, wl, wr)
        print(J, O, I)


if __name__ == '__main__':
    main()
