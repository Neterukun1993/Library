# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.PersistentStack import PersistentStack


def main():
    n = 10
    ps = PersistentStack()
    versions = [ps]

    for i in range(n):
        ps = versions[-1].push(i)
        versions.append(ps)

    for i in range(n + 1):
        ps = versions[i]
        for j in reversed(range(i)):
            assert(ps.top() == j)
            ps = ps.pop()
        assert(ps.top() is None)


if __name__ == '__main__':
    main()
    print("Hello World")
