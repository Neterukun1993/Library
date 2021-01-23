def tsp(matrix):
    INF = 10 ** 18
    n = len(matrix)
    dp = [[INF] * n for i in range(1 << n)]
    dp[1 << 0][0] = 0

    for bit_state in range(1 << n):
        for i in range(n):
            if not((bit_state >> i) & 1):
                continue
            for j in range(n):
                if (bit_state >> j) & 1:
                    continue
                new_state = bit_state | (1 << j)
                if dp[new_state][j] > dp[bit_state][i] + matrix[i][j]:
                    dp[new_state][j] = dp[bit_state][i] + matrix[i][j]

    ans = INF
    last = -1
    for i in range(n):
        if ans > dp[(1 << n) - 1][i] + matrix[i][0]:
            ans = dp[(1 << n) - 1][i] + matrix[i][0]
            last = i
    if ans == INF:
        return ans, []

    path = [last]
    v = last
    bit_state = (1 << n) - 1
    while v != 0:
        for prv_v in range(n):
            if (bit_state >> prv_v) & 1 and dp[bit_state][v] == dp[bit_state ^ (1 << v)][prv_v] + matrix[prv_v][v]:
                path.append(prv_v)
                bit_state -= 1 << v
                v = prv_v
                break
    return ans, path[::-1]
