# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.LazyBinaryTrie import LazyBinaryTrie
from misc.xorshift import xorshift32


def main():
    rand32 = xorshift32()
    lbt = LazyBinaryTrie()
    s = set()

    for _ in range(10000):
        # add
        val = rand32()
        lbt.add(val)
        s.add(val)

        # all_xor
        val = rand32()
        lbt.all_xor(val)
        s = set(v ^ val for v in s)

        # get_xor_min
        val = rand32()
        ans1 = lbt.get_xor_min(val)
        ans2 = min(v ^ val for v in s)
        assert(ans1 == ans2)


if __name__ == '__main__':
    main()
    print("Hello World")
