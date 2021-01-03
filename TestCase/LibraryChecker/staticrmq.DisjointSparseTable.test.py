# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.DisjointSparseTable import DisjointSparseTable


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]

    st = DisjointSparseTable(a, min)
    ans = []
    for l, r in queries:
        ans.append(st.fold(l, r))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
