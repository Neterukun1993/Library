def is_prime(x):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    for k in range(3, int(x ** 0.5) + 1, 2):
        if x % k == 0:
            return False
    return True
