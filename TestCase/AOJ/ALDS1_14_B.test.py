# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
from String.RollingHash import RollingHash


def main():
    t = input()
    p = input()

    rht = RollingHash(t)
    rhp = RollingHash(p)
    for l in range(len(t)):
        r = l + len(p)
        if r <= len(t) and rht.get_hash(l, r) == rhp.get_hash(0, len(p)):
            print(l)


if __name__ == '__main__':
    main()
