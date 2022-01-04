# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A
import sys
input = sys.stdin.buffer.readline

from Flow.MaxFlow import MaxFlow


def main():
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(e)]

    mf = MaxFlow(v)
    for fr, to, cap in edges:
        mf.add_edge(fr, to, cap)

    print(mf.max_flow(0, v - 1, 10 ** 9))


if __name__ == '__main__':
    main()
