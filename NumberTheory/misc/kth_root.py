def kth_root(a, k):
    res = int(pow(a, 1 / k))
    while pow(res + 1, k) <= a:
        res += 1
    while pow(res, k) > a:
        res -= 1
    return res
