from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree


def inversion_number(array):
    comp = {val: i for i, val in enumerate(sorted(set(array)))}
    for i, val in enumerate(array):
        array[i] = comp[val]
    max_val = max(array)
    bit = BinaryIndexedTree(max_val + 1)
    inv_num = 0
    for i in array:
        bit.add(i, 1)
        inv_num += bit.sum(i + 1, max_val + 1)
    return inv_num
