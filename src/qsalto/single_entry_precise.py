
from scipy.special import comb as scomb


try:
    import mpmath as mp
except ImportError:
    import mp_not_available
    mp = mp_not_available.mp_error()


def comb(n, k):
    return scomb(n, k, exact=True)


def M(n: int, i: int, j: int):
    sum = 0
    for l in range(i + 1):
        sum += comb(n - j, i - l) * comb(j, l) * (-1)**l * 3**(i - l)
    return mp.mpf(sum) / 2**n


def M1(n: int, i: int, j: int):
    if i == n - j:
        return mp.mpf(1)
    return mp.mpf(0)


def M2(n: int, i: int, j: int):
    if i != j:
        return 0.
    if (n - i) % 2 == 0:
        return mp.mpf(1)
    return mp.mpf(-1)


def T2(n: int, i: int, j: int):
    value = M(n, i, j)
    if j % 2 == 1:
        value *= -1
    return value


def iT2(n: int, i: int, j: int):
    value = M(n, i, j)
    if i % 2 == 1:
        value *= -1
    return value


def T1(n: int, i: int, j: int):
    return mp.mpf(comb(n - j, n - i)) * mp.power(2, n - i) / comb(n, i)


def iT1(n: int, i: int, j: int):
    return mp.mpf(comb(n - j, i - j) * (-1)**(i + j) * comb(n, j)) / 2**(n - j)


def T3(n: int, i: int, j: int):
    sum = 0
    for l in range(i + 1):
        sum += comb(n - j, i - l) * comb(j, l) * int((-1)**(j - l))
    return mp.mpf(sum * comb(n, j)) / 2**n


def iT3(n: int, i: int, j: int):
    sum = 0
    for l in range(i + 1):
        sum += comb(n - j, i - l) * comb(j, l) * (-1)**(i - l)
    return mp.mpf(sum) / comb(n, i)
