# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.UnionFind.UnionFindWithPotential import UnionFindWithPotential


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    INF = 10 ** 18
    ufp = UnionFindWithPotential(n)
    ans = []
    for flag, *query in queries:
        if flag == 0:
            x, y, p = query
            ufp.merge(x, y, p)
        else:
            x, y = query
            p = ufp.diff(x, y)
            ans.append(str(p) if p != INF else "?")

    print('\n'.join(ans))


if __name__ == '__main__':
    main()
