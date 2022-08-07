import math


def totient_sum(n, MOD):
    assert(n > 0)
    if n == 1: return 1
    if n == 2: return 2

    k = int((n / math.log2(math.log2(n))) ** (2 / 3)) + 1
    phi = [i for i in range(k)]

    for i in range(2, k):
        if phi[i] == i:
            for j in range(i, k, i):
                phi[j] -= phi[j] // i
                phi[j] %= MOD
    for i in range(k - 1):
        phi[i + 1] += phi[i]
        phi[i + 1] %= MOD

    phi2 = [0] * ((n + k - 2) // (k - 1))
    for i in range(1, len(phi2)):
        phi2[i] = (n // i) * (n // i + 1) // 2 % MOD

    for i in reversed(range(1, len(phi2))):
        cur = n // i
        j = 2
        while cur // j != cur // (j + 1) and j <= cur:
            if i * j >= len(phi2):
                phi2[i] -= phi[cur // j]
            else:
                phi2[i] -= phi2[i * j]
            phi2[i] %= MOD
            j += 1
        for arg in reversed(range(1, cur // j + 1)):
            if arg < k:
                phi2[i] -= (cur // arg - cur // (arg + 1)) * phi[arg]
            else:
                phi2[i] -= (cur // arg - cur // (arg + 1)) * phi2[n // arg]
            phi2[i] %= MOD

    return phi2[1]
