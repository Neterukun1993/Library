# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.List.SplayTreeList import SplayTreeList


def main():
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    stl = SplayTreeList()
    size = 0
    idx = 0

    for i in range(q):
        if queries[i][0] == 0:
            _, x = queries[i]
            stl.insert(idx, x)
            size += 1
            assert(size == len(stl))
        elif queries[i][0] == 1:
            _, d = queries[i]
            idx += d
        else:
            stl.delete(idx)
            size -= 1
            assert(size == len(stl))

    res = []
    for i in range(len(stl)):
        res.append(stl[i])

    new_stl = SplayTreeList()
    for _ in range(len(stl)):
        new_stl.insert(0, 0)
    for i, val in enumerate(res):
        new_stl[i] = val

    for i, val in enumerate(res):
        assert(val == new_stl[i])
        print(val)


if __name__ == '__main__':
    main()
