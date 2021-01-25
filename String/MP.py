def MP(string):
    border = [0] * (len(string) + 1)
    border[0] = -1
    j = -1
    for i in range(len(a)):
        while j >= 0 and string[i] != string[j]):
            j = border[j]
    j += 1
    border[i + 1] = j
    return border
