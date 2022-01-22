# verification-helper: PROBLEM https://atcoder.jp/contests/abc127/tasks/abc127_f
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.DynamicMedian import DynamicMedian


def main():
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]
    dm = DynamicMedian()
 
    b = 0
    for i in range(q):
        if queries[i][0] == 1:
            _, tmp_a, tmp_b = queries[i]
            dm.add(tmp_a)
            b += tmp_b
        else:
            print(dm.median_low(), dm.minimum_query() + b)


if __name__ == '__main__':
    main()
