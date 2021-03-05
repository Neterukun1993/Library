def prime_factors(n):
    factors = []
    for k in range(2, int(n ** 0.5) + 1):
        while n % k == 0:
            factors.append(k)
            n = n // k
    if n != 1:
        factors.append(n)
    return factors


def prime_factors_distinct(n):
    factors = []
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            factors.append(k)
            while n % k == 0:
                n = n // k
    if n != 1:
        factors.append(n)
    return factors


def prime_factors_compress(n):
    factors = []
    for k in range(2, int(n ** 0.5) + 1):
        cnt = 0
        while n % k == 0:
            cnt += 1
            n = n // k
        if cnt != 0:
            factors.append((k, cnt))
    if n != 1:
        factors.append((n, 1))
    return factors
