# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]

    bit = BinaryIndexedTree(n)
    bit.build(a)
    ans = []
    for flag, l, r in queries:
        if flag:
            ans.append(bit.sum(l, r))
        else:
            bit.add(l, r)  # l = index, r = val

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
