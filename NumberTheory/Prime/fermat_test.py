import random


def fermat_test(n, rep=100):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if n == 1:
        return False
    if n == 2:
        return True
    for _ in range(rep):
        a = random.randint(2, n - 1)
        if gcd(a, n) != 1:
            # a と n が互いに素ではない時点で n は合成数
            # カーマイケル数を素数と誤判定させるために continue している
            continue
        if pow(a, n - 1, n) != 1:
            return False
    return True
