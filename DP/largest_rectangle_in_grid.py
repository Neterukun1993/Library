from DP.largest_rectangle_in_histogram import largest_rectangle_in_histogram


def largest_rectangle_in_grid(grid, wall='#'):
    h = len(grid)
    w = len(grid[0])

    hists = [[0] * w for i in range(h)]
    for j in range(w):
        if grid[0][j] != wall:
            hists[0][j] = 1

    for i in range(1, h):
        for j in range(w):
            if grid[i][j] != wall:
                hists[i][j] = hists[i - 1][j] + 1

    ans = 0
    for hist in hists:
        ans = max(largest_rectangle_in_histogram(hist), ans)
    return ans
