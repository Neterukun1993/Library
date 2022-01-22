# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.List.SkipList import SkipList


def main():
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    sl = SkipList()
    idx = 0

    for i in range(q):
        if queries[i][0] == 0:
            _, x = queries[i]
            sl.insert(idx, x)
        elif queries[i][0] == 1:
            _, d = queries[i]
            idx += d
        else:
            sl.delete(idx)

    for res in sl.dump():
        print(res)


if __name__ == '__main__':
    main()
