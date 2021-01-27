def montmort_number(n, MOD):
    dp = [0] * (n + 1)
    if n >= 2:
        dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
        dp[i] %= MOD
    return dp


def montmort_number2(n, MOD):
    dp = [0] * (n + 1)
    for i in range(1, n):
        dp[i + 1] = (i + 1) * dp[i] + (-1) ** ((i + 1) & 1)
        dp[i + 1] %= MOD
    return dp
