MOD = 998244353


def linear_equations(matrix, vector):
    n = len(matrix)
    m = len(matrix[0])

    if len(vector) != n:
        raise RuntimeError('The number of rows of the matrix and the length of the vector must be the same.')
    if any(len(row) != m for row in matrix):
        raise RuntimeError('The number of columns of the matrix must be the same.')

    # 拡大係数行列を作成
    A = [matrix[i] + [vector[i]] for i in range(n)]

    # ピボットとして選択された列と選択されなかった列
    pivot_cols = []
    no_pivot_cols = []

    # 掃き出し法
    def _gauss_jordan():
        rank = 0
        for col in range(m):
            # ピボットを探す
            pivot = -1
            for row in range(rank, n):
                if A[row][col] != 0:
                    pivot = row
                    break

            # ピボットがない場合には次の列に
            if pivot == -1:
                no_pivot_cols.append(col)
                continue
            pivot_cols.append(col)

            # 行をスワップ
            A[pivot], A[rank] = A[rank], A[pivot]

            # ピボットの値を 1 にする
            inv = pow(A[rank][col], MOD - 2, MOD)
            for col2 in range(m + 1):
                A[rank][col2] *= inv
                A[rank][col2] %= MOD

            # ピボットのある列の値がすべて 0 になるように掃き出す
            for row in range(n):
                if row == rank or A[row][col] == 0:
                    continue
                fac = A[row][col]
                for col2 in range(m + 1):
                    A[row][col2] -= A[rank][col2] * fac
                    A[row][col2] %= MOD

            rank += 1

        return rank

    rank = _gauss_jordan()
    for row in range(rank, n):
        if A[row][m] != 0:
            # 解が存在しない場合
            return -1, [], []

    dimension = m - rank  # 解が一意の場合は 0, 解が無数に存在する場合は 1 以上

    # 解を1つ求める
    result = [0] * m
    for i in range(rank):
        result[pivot_cols[i]] = A[i][m]

    # 基底ベクトルを求める
    basis_vectors = []

    for i in no_pivot_cols:
        vec = [0] * m
        vec[i] = 1
        for j in range(rank):
            vec[pivot_cols[j]] = -A[j][i] % MOD
        basis_vectors.append(vec)

    return dimension, result, basis_vectors
