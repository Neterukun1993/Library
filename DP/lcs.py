def lcs(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i, chr_s in enumerate(s):
        for j, chr_t in enumerate(t):
            if chr_s == chr_t:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    res = []
    i, j = len(s), len(t)
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            res.append(s[i - 1])
            i -= 1
            j -= 1
    return ''.join(reversed(res))
