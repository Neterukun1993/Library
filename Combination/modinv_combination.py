class Combination:
    def __init__(self, n, MOD):
        self.f = [1]
        for i in range(1, n + 1):
            self.f.append(self.f[-1] * i % MOD)
        self.inv_f = [0] * (n + 1)
        self.inv_f[n] = pow(self.f[n], MOD - 2, MOD)
        for i in reversed(range(n)):
            self.inv_f[i] = self.inv_f[i + 1] * (i + 1) % MOD
        self.MOD = MOD

    def inv(self, k):
        """get inverse(k)"""
        return (self.inv_f[k] * self.f[k - 1]) % self.MOD

    def fact(self, k):
        """get k!"""
        return self.f[k]

    def inv_fact(self, k):
        """get inverse(k!)"""
        return self.inv_f[k]

    def perm(self, k, r):
        """get kPr"""
        if k < r:
            return 0
        return (self.f[k] * self.inv_f[k - r]) % self.MOD

    def comb(self, k, r):
        """get kCr"""
        if k < r:
            return 0
        return (self.f[k] * self.inv_f[k - r] % self.MOD
                * self.inv_f[r]) % self.MOD


def combination(k, r, MOD):
    """kCr O(r)"""
    if k < r:
        return 0
    r = min(r, k - r)
    numer, denom = 1, 1
    for l in range(r):
        numer *= (k - l)
        numer %= MOD
        denom *= l + 1
        denom %= MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD
