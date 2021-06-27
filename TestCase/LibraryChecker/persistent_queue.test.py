# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_queue
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.BankersQueue import BankersQueue


def main():
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    bq = BankersQueue()
    states = [None] * (q + 1)
    states[-1] = bq

    ans = []
    for i, (flag, *query) in enumerate(queries):
        if flag == 0:
            t, x = query
            states[i] = states[t].push(x)
        else:
            t = query[0]
            ans.append(states[t].front())
            states[i] = states[t].pop()

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
