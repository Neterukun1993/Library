# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1068
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.SparseTable2D import SparseTable2D


def main():
    ans = []
    while True:
        try:
            r, c, q = map(int, input().split())
            grid = [list(map(int, input().split())) for i in range(r)]
            queries = [list(map(int, input().split())) for i in range(q)]
     
            sp = SparseTable2D(grid, min)
            for hl, wl, hr, wr in queries:
                ans.append(sp.fold(hl, hr + 1, wl, wr + 1))
        except:
            break
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
