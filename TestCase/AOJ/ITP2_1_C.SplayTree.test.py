# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.List.SplayTreeList import SplayTreeList


def main():
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    stl = SplayTreeList()
    idx = 0
    for i in range(q):
        if queries[i][0] == 0:
            _, x = queries[i]
            stl.insert(idx, x)
        elif queries[i][0] == 1:
            _, d = queries[i]
            idx += d
        else:
            stl.delete(idx)

    for i in range(len(stl)):
        print(stl[i])


if __name__ == '__main__':
    main()
