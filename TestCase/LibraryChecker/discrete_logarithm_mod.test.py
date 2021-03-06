# verification-helper: PROBLEM https://judge.yosupo.jp/problem/discrete_logarithm_mod
import sys
input = sys.stdin.buffer.readline

from NumberTheory.ModularArithmetic.baby_step_giant_step import baby_step_giant_step


def main():
    t = int(input())
    info = [list(map(int, input().split())) for i in range(t)]

    for x, y, m in info:
        print(baby_step_giant_step(x, y, m))


if __name__ == '__main__':
    main()
