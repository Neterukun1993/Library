def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = extended_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y


def mod_inv(a, m):
    _, x, _ = extended_gcd(a, m)
    return x % m
