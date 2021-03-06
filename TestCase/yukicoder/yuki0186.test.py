# verification-helper: PROBLEM https://yukicoder.me/problems/no/186
import sys
input = sys.stdin.buffer.readline

from NumberTheory.ModularArithmetic.chinese_remainder_theorem import chinese_remainder_theorem


def main():
    info = [list(map(int, input().split())) for i in range(3)]

    x, y = list(zip(*info))
    r, m = chinese_remainder_theorem(x, y)
    if r == -1:
        print(-1)
    elif r == 0:
        print(m)
    else:
        print(r)


if __name__ == '__main__':
    main()
