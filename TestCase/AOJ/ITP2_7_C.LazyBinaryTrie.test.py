# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.LazyBinaryTrie import LazyBinaryTrie


def main():
    # __len__, __contains__, add, remove, kth_smallest, bisect_left, bisect_right
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    lbt = LazyBinaryTrie()
    ans = []
    for flag, *query in queries:
        if flag == 0:
            x = query[0]
            lbt.add(x)
            ans.append(len(lbt))
        elif flag == 1:
            x = query[0]
            ans.append(int(x in lbt))
        elif flag == 2:
            x = query[0]
            lbt.remove(x)
        else:
            vl, vr = query
            l = lbt.bisect_left(vl)
            r = lbt.bisect_right(vr)
            for i in range(l, r):
                ans.append(lbt.kth_smallest(i))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
