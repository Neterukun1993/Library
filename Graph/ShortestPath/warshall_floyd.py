from copy import deepcopy


def warshall_floyd(matrix):
    n = len(matrix)
    dist = deepcopy(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
