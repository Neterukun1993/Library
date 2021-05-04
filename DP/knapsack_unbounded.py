def knapsack_unbounded(w, items):
    n = len(items)
    dp = [-1] * (w + 1)
    dp[0] = 0

    for value, weight in items:
        for j in range(weight, w + 1):
            if dp[j - weight] == -1:
                continue
            else:
                dp[j] = max(dp[j], dp[j - weight] + value)
    return max(dp)
