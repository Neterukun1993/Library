# from collections import deque
from standard_library.collections import deque


def grid_bfs(grid, si, sj, wall="#"):
    INF = 10 ** 18
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    h, w = len(grid), len(grid[0])
    dist = [[INF] * w for i in range(h)]
    dist[si][sj] = 0
    que = deque([(si, sj)])
    while que:
        i, j = que.popleft()
        for di, dj in d:
            nxt_i, nxt_j = i + di, j + dj
            if not(0 <= nxt_i < h and 0 <= nxt_j < w):
                continue
            if grid[nxt_i][nxt_j] == wall:
                continue
            if dist[nxt_i][nxt_j] != INF:
                continue
            dist[nxt_i][nxt_j] = dist[i][j] + 1
            que.append((nxt_i, nxt_j))
    return dist
