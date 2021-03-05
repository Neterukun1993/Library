def segment_sieve(l, r):
    sqrt_r = int(r ** 0.5)
    is_prime_sqrt = [True] * (sqrt_r + 1)
    is_prime_sqrt[0] = False
    is_prime_sqrt[1] = False
    is_prime_tbl = [True] * (r - l)
    if l == 0:
        is_prime_tbl[0] = False
        is_prime_tbl[1] = False
    if l == 1:
        is_prime_tbl[0] = False

    for i in range(2, sqrt_r + 1):
        if not is_prime_sqrt[i]:
            continue
        for j in range(2 * i, sqrt_r + 1, i):
            is_prime_sqrt[j] = False
        for j in range(max((l + i - 1) // i, 2) * i, r, i):
            is_prime_tbl[j - l] = False

    prime_list = [l + i for i, flag in enumerate(is_prime_tbl) if flag]
    return prime_list, is_prime_tbl
