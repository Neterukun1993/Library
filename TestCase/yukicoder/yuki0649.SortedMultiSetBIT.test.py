# verification-helper: PROBLEM https://yukicoder.me/problems/no/649
import sys
input = sys.stdin.buffer.readline

from DataStructure.SortedSet.SortedMultiSetBIT import SortedMultiSetBIT


def main():
    # add, remove, kth_smallest, kth_largest
    q, k = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    k -= 1
    cands = [query[0] for flag, *query in queries if flag == 1]
    sset = SortedMultiSetBIT(cands)

    ans = []
    for flag, *query in queries:
        if flag == 1:
            val = query[0]
            sset.add(val)
        else:
            if k < len(sset):
                val = sset.kth_smallest(k)
                assert(val == sset.kth_largest(len(sset) - k - 1))
                sset.remove(val)
                ans.append(val)
            else:
                ans.append(-1)

    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()
