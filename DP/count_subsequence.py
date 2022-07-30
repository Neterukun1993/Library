def count_subsequence(a, MOD):
    n = len(a)
    idx = {}
    dp = [0] * (n + 1)
    dp[0] = 1
    for i, val in enumerate(a):
        if val in idx:
            dp[i + 1] = 2 * dp[i] - dp[idx[val]]
        else:
            dp[i + 1] = 2 * dp[i]
        dp[i + 1] %= MOD
        idx[val] = i
    return dp[n]
