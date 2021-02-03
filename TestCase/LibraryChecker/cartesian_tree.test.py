# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.cartesian_tree import cartesian_tree


def main():
    n = int(input())
    a = list(map(int, input().split()))

    par = cartesian_tree(a)
    print(*[p if p != -1 else i for i, p in enumerate(par)])


if __name__ == '__main__':
    main()
