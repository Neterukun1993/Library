from bisect import bisect_left, bisect_right


def lis(array, strict=True):
    lis_array = [array[0]]
    for val in array[1:]:
        if val > lis_array[-1] or (not strict and val == lis_array):
            lis_array.append(val)
        else:
            lis_array[bisect_left(lis_array, val)] = val

    return lis_array
