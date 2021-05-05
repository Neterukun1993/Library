def levenshtein_distance(s, t):
    len_s = len(s)
    len_t = len(t)
    INF = 10 ** 18
    dp = [[INF] * (len_t + 1) for _ in range(len_s + 1)]
    for i in range(len_s + 1):
        dp[i][0] = i
    for j in range(len_t + 1):
        dp[0][j] = j

    for i in range(len_s):
        for j in range(len_t):
            # 変更操作
            if s[i] == t[j]:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
            else:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + 1)
            # 削除操作
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j + 1] + 1)
            # 挿入操作
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i + 1][j] + 1)

    return dp[len_s][len_t]
