# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0560
import sys
input = sys.stdin.readline

from DataStructure.AccumulateSum.AccumulateSum2D import AccumulateSum2D


def main():
    m, n = map(int, input().split())
    k = int(input())
    s = [input()[:-1] for i in range(m)]
    queries = [list(map(int, input().split())) for i in range(k)]

    matJ = [[0] * n for i in range(m)]
    matO = [[0] * n for i in range(m)]
    matI = [[0] * n for i in range(m)]

    for i, t in enumerate(s):
        for j, char in enumerate(t):
            if char == "J":
                matJ[i][j] += 1
            elif char == "O":
                matO[i][j] += 1
            else:
                matI[i][j] += 1

    accJ = AccumulateSum2D(matJ)
    accO = AccumulateSum2D(matO)
    accI = AccumulateSum2D(matI)
    for hl, wl, hr, wr in queries:
        hl -= 1
        wl -= 1
        J = accJ.sum(hl, hr, wl, wr)
        O = accO.sum(hl, hr, wl, wr)
        I = accI.sum(hl, hr, wl, wr)
        print(J, O, I)


if __name__ == '__main__':
    main()
