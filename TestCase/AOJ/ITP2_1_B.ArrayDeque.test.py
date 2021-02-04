# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_B
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.ArrayDeque import ArrayDeque


def main():
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    dq = ArrayDeque()
    ans = []
    for flag, *query in queries:
        if flag == 0:
            d, x = query
            if d == 0:
                dq.appendleft(x)
            else:
                dq.append(x)
        elif flag == 1:
            p = query[0]
            ans.append(dq[p])
        else:
            d = query[0]
            if d == 0:
                dq.popleft()
            else:
                dq.pop()

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
