# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_D
import sys
input = sys.stdin.buffer.readline

from DataStructure.SortedSet.SortedMultiSetBTree import SortedMultiSetBTree


def main():
    # __len__, add, remove, iterate
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    ssbt = SortedMultiSetBTree()
    cnts = {}
    ans = []
    for flag, *query in queries:
        if flag == 0:
            x = query[0]
            ssbt.add(x)
            cnts[x] = cnts.get(x, 0) + 1
            ans.append(len(ssbt))
        elif flag == 1:
            x = query[0]
            cnts[x] = cnts.get(x, 0)
            ans.append(cnts[x])
        elif flag == 2:
            x = query[0]
            cnts[x] = cnts.get(x, 0)
            for _ in range(cnts[x]):
                ssbt.remove(x)
            cnts[x] = 0
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
