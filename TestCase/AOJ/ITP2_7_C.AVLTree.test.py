# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.SortedSet.SortedSetAVLTree import SortedSetAVLTree


def main():
    # __len__, __contains__, add, remove, iterate
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    ssavl = SortedSetAVLTree()
    ans = []
    for flag, *query in queries:
        if flag == 0:
            x = query[0]
            ssavl.add(x)
            ans.append(len(ssavl))
        elif flag == 1:
            x = query[0]
            ans.append(int(x in ssavl))
        elif flag == 2:
            x = query[0]
            ssavl.remove(x)
        else:
            vl, vr = query
            for val in ssavl.iterate(vl):
                if val <= vr:
                    ans.append(val)
                else:
                    break

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
