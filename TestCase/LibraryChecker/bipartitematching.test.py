# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching
import sys
input = sys.stdin.buffer.readline

from Flow.BipartiteGraph import BipartiteGraph


def main():
    l, r, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    bg = BipartiteGraph(l, r)
    for vl, vr in edges:
        bg.add_edge(vl, vr)

    ans = bg.maximum_matching()
    edges = bg.matching_edges()

    print(ans)
    for res in edges:
        print(*res)


if __name__ == '__main__':
    main()
