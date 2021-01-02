# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.SegmentTree import SegmentTree


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    e = (1 << 31) - 1
    st = SegmentTree(n, min, e)
    ans = []
    for flag, x, y in queries:
        if flag == 0:
            st[x] = y
        else:
            l, r = x, y + 1
            ans.append(st.fold(l, r))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
