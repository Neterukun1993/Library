# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.AccumulateSum.AccumulateSumLR import AccumulateSumLR


def bruteforce_test(array, n):
    acc_lr = AccumulateSumLR(array, min, n)
    for r in range(1, n + 1):
        assert(acc_lr.left_fold(r) == min(array[:r]))
    for l in range(n):
        assert(acc_lr.right_fold(l) == min(array[l:]))
    for i in range(n):
        val = n
        if i != 0:
            val = min(min(array[0:i]), val)
        if i != n - 1:
            val = min(min(array[i + 1:n]), val)
        assert(acc_lr.fold(i) == val)


def test_asc():
    n = 100
    array = [i for i in range(n)]
    bruteforce_test(array, n)


def test_desc():
    n = 100
    array = [i for i in reversed(range(n))]
    bruteforce_test(array, n)


def main():
    test_asc()
    test_desc()


if __name__ == '__main__':
    main()
    print("Hello World")
