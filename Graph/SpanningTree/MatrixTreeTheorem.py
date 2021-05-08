class MatrixTreeTheorem:
    def __init__(self, n):
        self.n = n
        self.lap_mat = [[0] * n for i in range(n)]

    def _determinant(self, mat, MOD):
        n = len(mat)
        det, rank = 1, 0
        for col in range(n):
            pivot = -1
            for row in range(col, n):
                if mat[row][col] != 0:
                    pivot = row
                    break
            if pivot == -1:
                return 0
            if pivot != rank:
                mat[rank], mat[pivot] = mat[pivot], mat[rank]
                det *= -1
            det *= mat[rank][rank]
            det %= MOD
            inv = pow(mat[rank][rank], MOD - 2, MOD)
            for col2 in range(col, n):
                mat[rank][col2] = mat[rank][col2] * inv % MOD
            for row in range(rank + 1, n):
                fac = mat[row][col]
                for col2 in range(col, n):
                    mat[row][col2] -= mat[rank][col2] * fac
                    mat[row][col2] %= MOD
            rank += 1
        return det

    def add_edge(self, u, v):
        self.lap_mat[u][u] += 1
        self.lap_mat[v][v] += 1
        self.lap_mat[u][v] -= 1
        self.lap_mat[v][u] -= 1

    def count_st(self, MOD):
        mat = [[val for val in rows[:-1]] for rows in self.lap_mat[:-1]]
        return self._determinant(mat, MOD)
