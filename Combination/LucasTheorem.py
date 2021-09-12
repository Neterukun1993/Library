from Combination.modinv_combination import Combination


class LucasTheorem:
    def __init__(self, p):
        self.MOD = p
        self.cmb = Combination(p - 1, p)

    def _p_adic(self, n):
        res = []
        while n > 0:
            res.append(n % self.MOD)
            n //= self.MOD
        return res

    def comb(self, n, k):
        res = 1
        for ni, ki in zip(self._p_adic(n), self._p_adic(k)):
            res *= self.cmb.comb(ni, ki)
            res %= self.MOD
        return res
