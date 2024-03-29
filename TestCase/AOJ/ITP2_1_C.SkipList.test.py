# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.List.SkipList import SkipList


def main():
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    sl = SkipList()
    size = 0
    idx = 0

    for i in range(q):
        if queries[i][0] == 0:
            _, x = queries[i]
            sl.insert(idx, x)
            size += 1
            assert(size == len(sl))
        elif queries[i][0] == 1:
            _, d = queries[i]
            idx += d
        else:
            sl.delete(idx)
            size -= 1
            assert(size == len(sl))

    res = []
    for i, val in enumerate(sl.dump()):
        assert(val == sl[i])
        res.append(val)

    new_sl = SkipList()
    for _ in range(len(sl)):
        new_sl.insert(0, 0)
    for i, val in enumerate(res):
        new_sl[i] = val

    for i, val in enumerate(res):
        assert(val == new_sl[i])
        print(val)


if __name__ == '__main__':
    main()
