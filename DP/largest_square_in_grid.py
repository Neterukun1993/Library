def largest_square_in_grid(grid, wall='#'):
    h = len(grid)
    w = len(grid[0])
    dp = [[0] * (w + 1) for i in range(h + 1)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == wall:
                dp[i + 1][j + 1] = 0
            else:
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                ans = max(dp[i + 1][j + 1], ans)
    return ans ** 2
