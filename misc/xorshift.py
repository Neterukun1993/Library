def xorshift32():
    y = 2463534242
    def inner():
        nonlocal y
        y = y ^ (y << 13 & 0xFFFFFFFF)
        y = y ^ (y >> 17 & 0xFFFFFFFF)
        y = y ^ (y << 5 & 0xFFFFFFFF)
        return y & 0xFFFFFFFF
    return inner
