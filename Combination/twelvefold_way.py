from Combination.modinv_combination import Combination


MOD = 10 ** 9 + 7
comb = Combination(10 ** 6 + 10, MOD)


def way1(ball, box):
    """ball: True / box: True / constraints: None
    -> ans = box ** ball
    """
    ans = pow(box, ball, MOD)
    return ans


def way2(ball, box):
    """ball: True / box: True / constraints: 1 or less
    -> ans = perm(box, ball)
    """
    if ball > box:
        return 0
    return comb.perm(box, ball)


def way3(ball, box):
    """ball: True / box: True / constraints: 1 or more
    -> ans = (包除原理)
    """
    if ball < box:
        return 0
    ans = 0
    for i in range(box + 1):
        ans += pow(-1, i, MOD) * comb.comb(box, i) * pow(box - i, ball, MOD)
        ans %= MOD
    return ans


def way4(ball, box):
    """ball: False / box: True / constraints: None
    -> ans = comb(box + ball - 1, ball)
    """
    return comb.comb(ball + box - 1, ball)

    # 区別するbox個の箱 -> 区別しない(box - 1)個の仕切に変換して解く


def way5(ball, box):
    """ball: False / box: True / constraints: 1 or less
    -> ans = comb(box, ball)
    """
    if ball > box:
        return 0
    return comb.comb(box, ball)


def way6(ball, box):
    """ball: False / box: True / constraints: 1 or more
    -> ans = combination(ball - 1, box - 1)
    """
    if ball < box:
        return 0
    return comb.comb(ball - 1, box - 1)

    # 考え方1
    # ボールを一列に並べたとき、(ball - 1)箇所ある隙間から、(box - 1)個を選ぶ

    # 考え方2
    # あらかじめ、すべての箱にボールを1つずつ配っておくと、
    # 区別しない(ball - box)個のボールを、区別するbox個の箱に配る通り数に帰着
    # -> way4(ball - box, box) と同等の問題となる


def way7(ball, box):
    """ball: True / box: False / constraints: None
    -> ans = B(ball, box) Bはベル数 / 計算量 O(ball * box)
    """
    # B[i][j] := S[i][j] + S[i][j - 1] + ... + S[i][0]
    # S[i][j] := i個(区別する)をkグループ(区別しない)に分ける場合の数
    S = [[0] * (box + 1) for i in range(ball + 1)]
    S[0][0] = 1
    for i in range(ball):
        for j in range(box):
            S[i + 1][j + 1] = S[i][j] + S[i][j + 1] * (j + 1)
            S[i + 1][j + 1] %= MOD
    B_ij = sum(S[ball][0:box + 1]) % MOD
    return B_ij


def way8(ball, box):
    """ball: True / box: False / constraints: 1 or less
    -> ans = int(ボールの数 <= 箱の数)
    """
    return int(ball <= box)


def way9(ball, box):
    """ball: True / box: False / constraints: 1 or more
    -> ans = S(ball, box) Sはスターリング数 / 計算量 O(ball * box)
    """
    if ball < box:
        return 0

    # S[i][j] := i個(区別する)をkグループ(区別しない)に分ける場合の数
    S = [[0] * (box + 1) for i in range(ball + 1)]
    S[0][0] = 1
    for i in range(ball):
        for j in range(box):
            S[i + 1][j + 1] = S[i][j] + S[i][j + 1] * (j + 1)
            S[i + 1][j + 1] %= MOD
    return S[ball][box]


def way10(ball, box):
    """ball: False / box: False / constraints: None
    ans = P(ball, box) Pは分割数 / 計算量 O(ball * box)
    """
    # P[i][j] := 整数iを順序を区別せずに「j以下の自然数」の和に分ける場合の数
    P = [[0] * (ball + 1) for _ in range(ball + 1)]
    for j in range(ball + 1):
        P[0][j] = 1
    for i in range(ball):
        for j in range(ball):
            if i - j >= 0:
                P[i + 1][j + 1] = (P[i + 1][j] + P[i - j][j + 1]) % MOD
            else:
                P[i + 1][j + 1] = P[i + 1][j]
    return P[ball][min(box, ball)]


def way11(ball, box):
    """ball: False / box: False / constraints: 1 or less
    -> ans = int(ボールの数 <= 箱の数)
    """
    return int(ball <= box)


def way12(ball, box):
    """ball: False / box: False / constraints: 1 or more
    ans = P(ball - box, box) Pは分割数 / 計算量 O(ball * box)
    """
    if ball < box:
        return 0

    # P[i][j] := 整数iを順序を区別せずに「j以下の自然数」の和に分ける場合の数
    diff = ball - box
    P = [[0] * (diff + 1) for _ in range(diff + 1)]
    for j in range(diff + 1):
        P[0][j] = 1
    for i in range(diff):
        for j in range(diff):
            if i - j >= 0:
                P[i + 1][j + 1] = (P[i + 1][j] + P[i - j][j + 1]) % MOD
            else:
                P[i + 1][j + 1] = P[i + 1][j]
    return P[diff][min(diff, box)]

    # あらかじめ、すべての箱にボールを1つずつ配っておくと
    # 区別しない(ball - box)個のボールを、区別しないbox個の箱に配る通り数に帰着
    # -> way11(ball - box, box) と同等の問題となる
