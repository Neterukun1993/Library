# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
import sys
input = sys.stdin.readline

from DataStructure.Heap.PersistentLeftistHeap import LeftistHeap


def main():
    lh = LeftistHeap()
    ans = []
    while True:
        a = input()
        if a[0] == "i":
            lh = lh.insert(-int(a[7:]), None)
        elif a[2] == "t":
            res, _ = lh.find_min
            lh = lh.delete_min()
            ans.append(-res)
        else:
            break

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
