def knapsack_bounded(w, items):
    n = len(items)
    dp = [0] * (w + 1)
    deq = [0] * (w + 1)
    deqv = [0] * (w + 1)
    for value, weight, qty in items:
        for rem in range(weight):
            s, t = 0, 0
            j = 0
            while j * weight + rem <= w:
                val = dp[j * weight + rem] - j * value
                while s < t and deqv[t - 1] <= val:
                    t -= 1
                deq[t] = j
                deqv[t] = val
                t += 1
                dp[j * weight + rem] = deqv[s] + j * value
                if deq[s] == j - qty:
                    s += 1
                j += 1
    return dp
