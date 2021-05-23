# verification-helper: PROBLEM https://yukicoder.me/problems/no/430
from String.Patricia import Patricia


def main():
    s = input()
    m = int(input())
    c = [input() for i in range(m)]

    pat = Patricia()
    for string in c:
        pat.insert(string)

    ans = 0
    for i in range(len(s)):
        for length in range(1, 11):
            if i + length > len(s):
                break
            if pat.search(s[i:i + length]):
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()

