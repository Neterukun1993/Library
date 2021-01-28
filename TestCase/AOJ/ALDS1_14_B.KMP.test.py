# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
from String.KMP import KMP


def main():
    t = input()
    p = input()

    kmp = KMP(p)
    ans = kmp.match(t)
    if ans:
        print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
