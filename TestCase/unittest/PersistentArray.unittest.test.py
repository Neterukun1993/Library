# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.PersistentArray import (
    PersistentArray,
    init_persistent_array
)


def main():
    n = 100
    arr = [-1] * n
    per_arr = init_persistent_array(arr)

    versions = [per_arr]
    for i in range(n):
        per_arr = versions[-1].set(i, i)
        versions.append(per_arr)

    for i in range(n + 1):
        per_arr = versions[i]
        for j in range(n):
            if j < i:
                assert(per_arr.get(j) == j)
            else:
                assert(per_arr.get(j) == -1)


if __name__ == '__main__':
    main()
    print("Hello World")
