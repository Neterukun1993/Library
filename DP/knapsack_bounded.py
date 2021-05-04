from DataStructure.misc.SlidingWindowAggregation import SlidingWindowAggregation


def knapsack_bounded(w, items):
    n = len(items)
    dp = [0] * (w + 1)

    for value, weight, qty in items:
        for rem in range(weight):
            swag = SlidingWindowAggregation(max)
            j = 0
            while j * weight + rem <= w:
                swag.append(dp[j * weight + rem] - j * value)
                dp[j * weight + rem] = swag.all_fold() + j * value
                if len(swag) > qty:
                    swag.popleft()
                j += 1
    return max(dp)
