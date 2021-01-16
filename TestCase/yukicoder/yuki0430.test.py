# verification-helper: PROBLEM https://yukicoder.me/problems/no/430
from String.Trie import Trie


def main():
    s = input()
    m = int(input())
    c = [input() for i in range(m)]

    tr = Trie()
    for string in c:
        tr.insert(string)

    ans = 0
    for i in range(len(s)):
        for length in range(1, 11):
            if i + length > len(s):
                break
            if tr.search(s[i:i + length]):
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()

