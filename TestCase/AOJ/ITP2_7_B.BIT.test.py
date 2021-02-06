# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_B
import sys
input = sys.stdin.buffer.readline

from DataStructure.SortedSet.SortedSetBIT import SortedSetBIT


def main():
    # __len__, __contains__, add, remove
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    cands = [x for flag, x in queries if flag == 0]
    sset = SortedSetBIT(cands)
    ans = []
    for flag, x in queries:
        if flag == 0:
            sset.add(x)
            ans.append(len(sset))
        elif flag == 1:
            ans.append(int(x in sset))
        else:
            sset.remove(x)

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
