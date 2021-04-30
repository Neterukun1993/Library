def divisors(n):
    divs = []
    for k in range(1, int(n ** 0.5) + 1):
        if n % k == 0:
            divs.append(k)
            if k != n // k:
                divs.append(n // k)
    divs = sorted(divs)
    return divs
