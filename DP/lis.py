from bisect import bisect_left, bisect_right


def lis(array, strict=True):
    lis_array = [array[0]]
    bisect_ = bisect_left if strict else bisect_right

    for val in array[1:]:
        idx = bisect_(lis_array, val)
        if idx == len(lis_array):
            lis_array.append(val)
        else:
            lis_array[idx] = val

    return lis_array
