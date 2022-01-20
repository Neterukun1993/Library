# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B
import sys
input = sys.stdin.buffer.readline

from Flow.MinCostFlow import MinCostFlow


def main():
    n, m, f = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    mcf = MinCostFlow(n)
    for fr, to, c, d in edges:
        mcf.add_edge(fr, to, c, d)

    ans = mcf.min_cost_flow(0, n - 1, f)
    print(ans)


if __name__ == '__main__':
    main()
