def miller_rabin(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d & 1 == 0:
        s += 1
        d >>= 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if n <= a:
            break
        x = pow(a, d, n)
        if x == 1:
            continue
        for _ in range(s):
            if x == n - 1:
                break
            x = x * x % n
        else:
            return False
    return True
