def calc_next(small_characters):
    n = len(small_characters)
    nxt = [[-1] * 26 for i in range(n + 1)]

    for i in reversed(range(n)):
        for val in range(26):
            if val == ord(small_characters[i]) - 97:
                nxt[i][val] = i + 1
            else:
                nxt[i][val] = nxt[i + 1][val]
    return nxt


def substring_dp(small_characters, MOD):
    n = len(small_characters)
    nxt = calc_next(small_characters)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(n):
        for val in range(26):
            if nxt[i][val] == -1:
                continue
            dp[nxt[i][val]] += dp[i]
            dp[nxt[i][val]] %= MOD

    ans = 0
    for i in range(n + 1):  # 空文字 (i = 0 のとき) も含める。
        ans += dp[i]
        ans %= MOD
    return ans
