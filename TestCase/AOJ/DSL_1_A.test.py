# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.UnionFind.UnionFind import UnionFind


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    uf = UnionFind(n)
    ans = []
    for flag, x, y in queries:
        if flag == 0:
            uf.merge(x, y)
        else:
            ans.append(int(uf.same(x, y)))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
