# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.List.UnrolledLinkedList import UnrolledLinkedList


def main():
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    ull = UnrolledLinkedList()
    size = 0
    idx = 0

    for i in range(q):
        if queries[i][0] == 0:
            _, x = queries[i]
            ull.insert(idx, x)
            size += 1
            assert(size == len(ull))
        elif queries[i][0] == 1:
            _, d = queries[i]
            idx += d
        else:
            ull.delete(idx)
            size -= 1
            assert(size == len(ull))

    res = []
    for i, val in enumerate(ull.dump()):
        assert(val == ull[i])
        res.append(val)

    new_ull = UnrolledLinkedList()
    for _ in range(len(ull)):
        new_ull.insert(0, 0)
    for i, val in enumerate(res):
        new_ull[i] = val

    for i, val in enumerate(res):
        assert(val == new_ull[i])
        print(val)


if __name__ == '__main__':
    main()
