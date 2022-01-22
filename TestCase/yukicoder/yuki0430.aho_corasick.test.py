# verification-helper: PROBLEM https://yukicoder.me/problems/no/430
from String.AhoCorasick import AhoCorasick


def main():
    text = input()
    m = int(input())
    c = [input() for i in range(m)]

    ac = AhoCorasick()
    for string in c:
        ac.add(string)
    ac.build_pma()
    print(ac.match_count(text))


if __name__ == '__main__':
    main()

