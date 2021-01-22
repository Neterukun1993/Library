# verification-helper: PROBLEM https://yukicoder.me/problems/no/430
from String.RollingHash import RollingHash


def main():
    s = input()
    m = int(input())
    c = [input() for i in range(m)]

    rh = RollingHash(s)

    cnt = {}
    for string in c:
        rhc = RollingHash(string)
        hs = rhc.get_hash(0, len(string))
        cnt[hs] = cnt.get(hs, 0) + 1

    n = len(s)
    ans = 0
    for l in range(n):
        for length in range(11):
            r = l + length
            if r <= n:
                ans += cnt.get(rh.get_hash(l, r), 0)
    print(ans)


if __name__ == '__main__':
    main()
