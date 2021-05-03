# verification-helper: PROBLEM https://yukicoder.me/problems/no/187
import sys
input = sys.stdin.buffer.readline

from NumberTheory.ModularArithmetic.garner import pregarner, garner


def main():
    n = int(input())
    info = [list(map(int, input().split())) for i in range(n)]
    MOD = 10 ** 9 + 7

    x, y = list(zip(*info))
    x, y = list(x), list(y)

    lcm, x, y = pregarner(x, y, MOD)
    if sum(x) == 0 or lcm == -1:
        print(lcm)
    else:
        m = garner(x, y, MOD)
        print(m)


if __name__ == '__main__':
    main()
