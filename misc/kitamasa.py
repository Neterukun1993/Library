MOD = 10 ** 9 + 7
add = lambda a, b: (a + b) % MOD
e_add = lambda: 0
mul = lambda a, b: a * b % MOD
# e_mul = lambda: 1


def kitamasa(a, d, n):
    # n is 0-indexed
    def increment(cs):
        res = [e_add() for _ in range(k)]
        res[0] = mul(d[0], cs[-1])
        for i in range(1, k):
            res[i] = add(cs[i - 1], mul(d[i], cs[-1]))
        return res

    def double(cs):
        mat = []
        mat.append(cs)
        for i in range(k - 1):
            mat.append(increment(mat[-1]))
        res = [e_add() for _ in range(k)]
        for i in range(k):
            for j in range(k):
                res[j] = add(res[j], mul(mat[i][j], cs[i]))
        return res

    def dfs(cs, n):
        if n == k:
            return d
        if (n & 1 or n < k * 2):
            cs = dfs(cs, n - 1)
            res = increment(cs)
        else:
            cs = dfs(cs, n // 2)
            res = double(cs)
        return res

    k = len(d)
    if k > n:
        return a[n]
    coeffs = dfs(d, n)
    ans = e_add()
    for vc, va in zip(coeffs, a):
        ans = add(ans, mul(vc, va))
    return ans
