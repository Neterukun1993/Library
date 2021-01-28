def MP(s):
    border = [0] * (len(s) + 1)
    border[0] = -1
    j = -1
    for i in range(len(a)):
        while j >= 0 and s[i] != s[j]):
            j = border[j]
    j += 1
    border[i + 1] = j
    return border
