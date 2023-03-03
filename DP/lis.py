from bisect import bisect_left, bisect_right


def lis(array, strict=True):
    bisect_ = bisect_left if strict else bisect_right
    tmp = []
    idxs = [0] * len(array)

    for i, val in enumerate(array):
        idx = bisect_(tmp, val)
        if idx == len(tmp):
            tmp.append(val)
        else:
            tmp[idx] = val
        idxs[i] = idx

    lis_array = []
    j = len(tmp) - 1
    for i, val in reversed(list(enumerate(array))):
        if idxs[i] == j:
            lis_array.append(val)
            j -= 1
    return lis_array[::-1]


def lis_index(array, strict=True):
    lis_array = lis(array, strict)
    idxs = []

    i = 0
    for idx, val in enumerate(array):
        if i < len(lis_array) and lis_array[i] == val:
            idxs.append(idx)
            i += 1
    return idxs
