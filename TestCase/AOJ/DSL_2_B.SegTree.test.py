# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.SegmentTree import SegmentTree


def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    st = SegmentTree(n, lambda x, y: x + y, 0)
    ans = []
    for flag, x, y in queries:
        if flag == 0:
            i = x - 1
            st[i] = st[i] + y
        else:
            l, r = x - 1, y
            ans.append(st.fold(l, r))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
