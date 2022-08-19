# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.UnionFind.EnumerableUnionFind import EnumerableUnionFind


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    euf = EnumerableUnionFind(n)
    ans = []
    for flag, x, y in queries:
        if flag == 0:
            euf.merge(x, y)
        else:
            ans.append(int(euf.same(x, y)))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
