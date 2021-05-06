# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from String.run_length_encoding import encoding


def test(string):
    comp = encoding(string)
    res = ""
    for char, cnt in comp:
        res += char * cnt
    assert(res == string)


def main():
    string = ""
    test(string)

    string = "A"
    test(string)

    string = "AAAAA"
    test(string)

    string = "AABA"
    test(string)

    string = "AABBAABB"

    string = "ABCDE"
    test(string)


if __name__ == '__main__':
    main()
    print("Hello World")
