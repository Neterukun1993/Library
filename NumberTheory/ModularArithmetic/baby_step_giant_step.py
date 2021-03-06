def baby_step_giant_step(x, y, MOD):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    x %= MOD
    y %= MOD
    k, add, g = 1, 0, gcd(x, MOD)
    while g > 1:
        if y == k:
            return add
        if y % g:
            return -1
        y //= g
        MOD //= g
        add += 1
        k = (k * x // g) % MOD
        g = gcd(x, MOD)

    sqrtMOD = int(MOD ** 0.5) + 1
    baby = {}
    cur = y
    for i in range(sqrtMOD + 1):
        baby[cur] = i
        cur = (cur * x) % MOD

    xpow = pow(x, sqrtMOD, MOD)
    cur = k
    for i in range(1, sqrtMOD + 1):
        cur = (cur * xpow) % MOD
        if cur in baby:
            return sqrtMOD * i - baby[cur] + add

    return -1
