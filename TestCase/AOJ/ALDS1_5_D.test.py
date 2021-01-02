# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D
import sys
input = sys.stdin.readline

from DataStructure.BinaryIndexedTree.inversion_number import inversion_number


def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(inversion_number(a))


if __name__ == '__main__':
    main()

