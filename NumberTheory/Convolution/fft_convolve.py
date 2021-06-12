from cmath import pi, exp


def _fft(a, h):
    roots = [exp(2.0j * pi / 2 ** i) for i in range(h + 1)]
    for i in range(h):
        m = 1 << (h - i - 1)
        for j in range(1 << i):
            w = 1
            j *= 2 * m
            for k in range(m):
                a[j + k], a[j + k + m] = \
                    a[j + k] + a[j + k + m], (a[j + k] - a[j + k + m]) * w
                w *= roots[h - i]


def _ifft(a, h):
    iroots = [exp(-2.0j * pi / 2 ** i) for i in range(h + 1)]
    for i in range(h):
        m = 1 << i
        for j in range(1 << (h - i - 1)):
            w = 1
            j *= 2 * m
            for k in range(m):
                a[j + k], a[j + k + m] = \
                    a[j + k] + a[j + k + m] * w, a[j + k] - a[j + k + m] * w
                w *= iroots[i + 1]
    n = 1 << h
    for i in range(n):
        a[i] /= n


def fft_convolve(a, b):
    len_ab = len(a) + len(b)
    n = 1 << (len(a) + len(b) - 1).bit_length()
    h = n.bit_length() - 1
    a = list(a) + [0] * (n - len(a))
    b = list(b) + [0] * (n - len(b))

    _fft(a, h), _fft(b, h)
    a = [va * vb for va, vb in zip(a, b)]
    _ifft(a, h)
    return [int(abs(a[i]) + 0.5) for i in range(len_ab - 1)]
