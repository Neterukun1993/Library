from NumberTheory.Basic.extended_gcd import extended_gcd


def linear_congruence(a, b, m):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if b % gcd(a, m) != 0:
        # 解なし
        return False, -1, -1
    g, x, y = extended_gcd(a, m)
    x *= b // g
    cycle = m // g
    x -= cycle * (x // cycle)
    return True, x, cycle
