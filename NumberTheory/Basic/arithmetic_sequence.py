class Arithmetic:
    @staticmethod
    def get(a0, d, i):
        return i * a0 + d

    @staticmethod
    def general_term(i, ai, j, aj):
        def gcd(a, b):
            while b: a, b = b, a % b
            return a

        assert(i != j)
        if i > j:
            i, j = j, i
        gcd_ = gcd(abs(j * ai - i * aj), j - i)
        rational_a0 = ((j * ai - i * aj) // gcd_, (j - i) // gcd_)
        gcd_ = gcd(abs(aj - ai), j - i)
        rational_d = ((aj - ai) // gcd_, (j - i) // gcd_)
        return rational_a0, rational_d

    @staticmethod
    def sum(a0, d, r):
        return r * a0 + d * (r - 1) * r // 2

    @staticmethod
    def range_sum(a0, d, l, r):
        return Arithmetic.sum(a0, d, r) - Arithmetic.sum(a0, d, l)
