def eratosthenes_sieve(n):
    is_prime_tbl = [True] * (n + 1)
    is_prime_tbl[0] = False
    is_prime_tbl[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime_tbl[i]:
            continue
        for j in range(2 * i, n + 1, i):
            is_prime_tbl[j] = False
    prime_list = [i for i, flag in enumerate(is_prime_tbl) if flag]
    return prime_list, is_prime_tbl
