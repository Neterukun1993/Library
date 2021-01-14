# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
import sys
input = sys.stdin.readline

from DataStructure.Heap.DAryHeap import DAryHeap


def main():
    hp = DAryHeap(D=3)
    ans = []
    while True:
        a = input()
        if a[0] == "i":
            hp.push(-int(a[7:]))
        elif a[2] == "t":
            ans.append(-hp.pop())
        else:
            break

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
