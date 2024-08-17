def get_f2_basis(array):
    base = []
    for value in array:
        for e in base:
            value = min(value, value ^ e)
        if value > 0:
            base.append(value)
    return base
