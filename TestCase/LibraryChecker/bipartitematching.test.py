# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching
import sys
input = sys.stdin.buffer.readline

from Flow.BipartiteMatching import BipartiteMatching


def main():
    l, r, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    bm = BipartiteMatching(l, r)
    for vl, vr in edges:
        bm.add_edge(vl, vr)

    ans = bm.maximum_matching()
    edges = bm.matching_edges()

    print(ans)
    for res in edges:
        print(*res)


if __name__ == '__main__':
    main()
