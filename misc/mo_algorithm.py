SIZE = 256


def mo_algorithm(n, q, intervals, add1, add2, rem1, rem2, get):
    orders = [((l // SIZE) << 40) + (r << 20) + i for i, (l, r) in enumerate(intervals)]
    orders.sort()
    answers = [0] * q
    nl, nr = 0, 0

    for order in orders:
        i = order & ((1 << 20) - 1)
        l, r = intervals[i]
        while nl > l:
            nl -= 1
            add1(nl)
        while nr < r:
            add2(nr)
            nr += 1
        while nl < l:
            rem1(nl)
            nl += 1
        while nr > r:
            nr -= 1
            rem2(nr)
        answers[i] = get()
    return answers
