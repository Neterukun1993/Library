def z_algorithm(s):
    res = [0] * len(s)
    res[0] = len(s)
    i, j = 1, 0
    while i < len(s):
        while i + j < len(s) and s[j] == s[i + j]:
            j += 1
        res[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < len(s) and k + res[k] < j:
            res[i + k] = res[k]
            k += 1
        i, j = i + k, j - k
    return res
