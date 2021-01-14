# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1068
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.SparseTable2D import SparseTable2D


def main():
    ans = []
    try:
        while True:
            r, c, q = map(int, input().split())
            grid = [list(map(int, input().split())) for i in range(r)]
            queries = [list(map(int, input().split())) for i in range(q)]

            sp = SparseTable2D(grid, min)
            for hl, wl, hr, wr in queries:
                hr += 1
                wr += 1
                ans.append(sp.fold(hl, hr, wl, wr))
    except:
        print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
