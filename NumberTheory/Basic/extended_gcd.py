def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = extended_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y
