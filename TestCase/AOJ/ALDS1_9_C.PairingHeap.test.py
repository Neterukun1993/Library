# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
import sys
input = sys.stdin.readline

from DataStructure.Heap.PairingHeap import PairingHeap


def main():
    ph = PairingHeap()
    ans = []
    while True:
        a = input()
        if a[0] == "i":
            ph.push(-int(a[7:]))
        elif a[2] == "t":
            ans.append(-ph.pop())
        else:
            break

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
