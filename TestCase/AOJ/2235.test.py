# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2235
import sys
input = sys.stdin.readline

from DataStructure.UnionFind.OfflineDynamicConnectivity import OfflineDynamicConnectivity


def main():
    n, k = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(k)]

    question_cnt = 0
    questions = []
    for flag, u, v in queries:
        if flag == 3:
            question_cnt += 1
            questions.append((u, v))

    odc = OfflineDynamicConnectivity(question_cnt, questions, n)

    t = 0
    for flag, u, v in queries:
        if flag == 3:
            t += 1
            continue
        if t == question_cnt:
            continue
        if flag == 1:
            odc.insert(t, u, v)
        else:
            odc.erase(t, u, v)

    odc.construct()
    res = odc.run()

    if not res:
        pass
    else:
        print("\n".join(["YES" if ans else "NO" for ans in res]))


if __name__ == '__main__':
    main()
