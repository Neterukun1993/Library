def matrix_pow(A, k, MOD):
    def matrix_mul(A, B, MOD):
        C = [[0] * size for _ in range(size)]
        for i in range(size):
            for k in range(size):
                for j in range(size):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
        return C

    if len(A) != len(A[0]):
        raise ValueError('square matrix expected')

    size = len(A)
    B = [[0] * size for _ in range(size)]
    for i in range(size):
        B[i][i] = 1
    while k > 0:
        if k & 1:
            B = matrix_mul(A, B, MOD)
        A = matrix_mul(A, A, MOD)
        k = k // 2
    return B


def matvec_mul(A, vec, MOD):
    if len(A[0]) != len(vec):
        raise ValueError('dimension mismatch between matrix and vector')

    h, w = len(A), len(A[0])
    res_vec = [0] * h
    for i in range(h):
        for j in range(w):
            res_vec[i] += A[i][j] * vec[j]
            res_vec[i] %= MOD
    return res_vec
