def euler_phi(n):
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            ans -= ans // i
    if n > 1:
        ans -= ans // n
    return ans
