# verification-helper: PROBLEM https://judge.yosupo.jp/problem/set_xor_min
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.BinaryTrie import BinaryTrie


def main():
    n = int(input())
    query = [list(map(int, input().split())) for i in range(n)]

    bt = BinaryTrie()
    ans = []
    for q, x in query:
        if q == 0:
            bt.insert(x)
        elif q == 1:
            bt.delete(x)
        else:
            ans.append(bt.get_xor_min(x))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
