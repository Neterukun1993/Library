# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.UnionFind.EnumerableUnionFind import EnumerableUnionFind


def test_initialize():
    n = 10
    euf = EnumerableUnionFind(n)
    for i in range(n):
        group = euf.enumerate(i)
        assert(len(group) == 1)
        assert(group[0] == i )


def test_merge_and_enumerate():
    n = 6
    euf = EnumerableUnionFind(n)

    # [0]
    # [1, 2]
    # [3, 4, 5]
    euf.merge(1, 2)
    euf.merge(3, 4)
    euf.merge(4, 5)

    for i in (0, ):
        group = euf.enumerate(i)
        assert(len(group) == 1)
        assert(0 in group)

    for i in (1, 2):
        group = euf.enumerate(i)
        assert(len(group) == 2)
        assert(1 in group and 2 in group)

    for i in (3, 4, 5):
        group = euf.enumerate(i)
        assert(len(group) == 3)
        assert(3 in group and 4 in group and 5 in group)

    # [0, 1, 2, 3, 4, 5]
    euf.merge(0, 1)
    euf.merge(2, 3)

    for i in (0, 1, 2, 3, 4, 5):
        group = euf.enumerate(i)
        assert(len(group) == 6)
        assert(0 in group and 1 in group and 2 in group)
        assert(3 in group and 4 in group and 5 in group)


def main():
    test_initialize()
    test_merge_and_enumerate()


if __name__ == '__main__':
    main()
    print("Hello World")
