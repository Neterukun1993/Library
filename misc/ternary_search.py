def ternary_search_max(l, r, evaluate):
    EPS = 10 ** (-6)
    while r - l > EPS:
        midl = l + (r - l) / 3
        midr = r - (r - l) / 3
        if evaluate(midl) < evaluate(midr):
            l = midl
        else:
            r = midr
    return l, evaluate(l)


def ternary_search_min(l, r, evaluate):
    EPS = 10 ** (-6)
    while r - l > EPS:
        midl = l + (r - l) / 3
        midr = r - (r - l) / 3
        if evaluate(midl) > evaluate(midr):
            l = midl
        else:
            r = midr
    return l, evaluate(l)


def ternary_search_intmax(l, r, evaluate):
    while (r - l) > 1:
        mid = (r + l) // 2
        # 凸の左側に平坦が存在するときは不等号に = をつける。
        # 凸の左右に平坦が存在するときは解けない。
        if evaluate(mid) - evaluate(mid - 1) > 0:
            l = mid
        else:
            r = mid
    return l, evaluate(l)


def ternary_search_intmin(l, r, evaluate):
    while (r - l) > 1:
        mid = (r + l) // 2
        # 凸の右側に平坦が存在するときは不等号に = をつける。
        # 凸の左右に平坦が存在するときは解けない。
        if evaluate(mid) - evaluate(mid - 1) < 0:
            l = mid
        else:
            r = mid
    return l, evaluate(l)
