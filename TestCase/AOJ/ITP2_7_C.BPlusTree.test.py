# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C
import sys
input = sys.stdin.buffer.readline

from DataStructure.SortedSet.SortedSetBPlusTree import SortedSetBPlusTree


def main():
    # __len__, __contains__, add, remove, iterate
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    ssbt = SortedSetBPlusTree(B_SIZE=512)
    ans = []
    for flag, *query in queries:
        if flag == 0:
            x = query[0]
            ssbt.add(x)
            ans.append(len(ssbt))
        elif flag == 1:
            x = query[0]
            ans.append(int(x in ssbt))
        elif flag == 2:
            x = query[0]
            ssbt.remove(x)
        else:
            vl, vr = query
            for val in ssbt.iterate(vl):
                if val <= vr:
                    ans.append(val)
                else:
                    break

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
