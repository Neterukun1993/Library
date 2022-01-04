# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2313
import sys
input = sys.stdin.readline

from Flow.MaxFlow import MaxFlow


def main():
    # verify: add_edge, get_edge, change_edge, max_flow
    n, e, q = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(e)]
    queries = [list(map(int, input().split())) for i in range(q)]

    mf = MaxFlow(n)
    label = {}
    idx = 0
    for u, v in edges:
        u -= 1
        v -= 1
        if v < u:
            u, v = v, u
        label[u, v] = idx
        idx += 1
        mf.add_edge(u, v, 0)
        mf.change_edge(label[u, v], 2, 1)

    flow = mf.max_flow(0, n - 1, 10 ** 9)

    for flag, u, v in queries:
        u -= 1
        v -= 1
        if v < u:
            u, v = v, u
        if flag == 1:
            label[u, v] = idx
            idx += 1
            mf.add_edge(u, v, 0)
            mf.change_edge(label[u, v], 2, 1)
            flow += mf.max_flow(0, n - 1, 10 ** 9)
        else:
            i = label[u, v]
            if mf.get_edge(i)[3] == 2:
                val = mf.max_flow(u, v, 1)
                if val == 0:
                    mf.max_flow(n - 1, 0, 1)
                    mf.max_flow(u, v, 1)
                    flow -= 1
            elif mf.get_edge(i)[3] == 0:
                val = mf.max_flow(v, u, 1)
                if val == 0:
                    mf.max_flow(n - 1, 0, 1)
                    mf.max_flow(v, u, 1)
                    flow -= 1
            mf.change_edge(label[u, v], 0, 0)

        print(flow)


if __name__ == '__main__':
    main()
