def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def all_gcd(array):
    n = len(array)
    ans = array[0]
    for i in range(1, n):
        ans = gcd(ans, array[i])
    return ans


def all_lcm_int(array):
    ans = array[0]
    for i in range(1, len(array)):
        ans = (ans * array[i]) // gcd(ans, array[i])
    return ans


def all_lcm_dict(array):
    primes = {}
    for num in array:
        for k in range(2, int(num ** 0.5) + 1):
            cnt = 0
            while num % k == 0:
                cnt += 1
                num //= k
            if cnt != 0:
                if k not in primes:
                    primes[k] = cnt
                else:
                    primes[k] = max(cnt, primes[k])
        if num != 1:
            if num not in primes:
                primes[num] = 1
    return primes
