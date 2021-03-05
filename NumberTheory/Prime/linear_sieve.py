def linear_sieve(n):
    prime_list = []
    mindiv_factor = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if mindiv_factor[i] == i:
            prime_list.append(i)
        for p in prime_list:
            if p * i > n or p > mindiv_factor[i]:
                break
            mindiv_factor[p * i] = p
    return prime_list, mindiv_factor


def prime_factors(n, mindiv_factor):
    pf = []
    while mindiv_factor[n] != 1:
        pf.append(mindiv_factor[n])
        n //= mindiv_factor[n]
    return pf
