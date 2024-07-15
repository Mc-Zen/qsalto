
import numpy as np
from scipy.special import comb as scomb


def comb(n, k):
    return scomb(n, k, exact=True)


def M(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for k in range(n + 1):
        for l in range(n + 1):
            sum = 0
            for j in range(n + 1):
                sum += comb(l, j) * comb(n-l, k-j) * \
                    3**(k - j) * (-1)**j
            K[k, l] = sum
    K *= 2**-n
    return K


def M1(n: int) -> np.ndarray:
    return np.fliplr(np.eye(n+1))


def M2(n: int) -> np.ndarray:
    return np.diag(np.resize([1, -1], n+1)[::-1])


def T2(n: int) -> np.ndarray:
    K = M(n)
    for col in range(1, n+1, 2):
        K[:, col] *= -1.
    return K


def iT2(n: int) -> np.ndarray:
    K = M(n)
    for row in range(1, n+1, 2):
        K[row] *= -1.
    return K


def T1(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for k in range(n + 1):
        for l in range(n + 1):
            K[k, l] = comb(n - l, n - k) / comb(n, k) * 2**(n - k)
    return K


def iT1(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for k in range(n + 1):
        for l in range(n + 1):
            K[k, l] = comb(n - l, k - l) * (-1)**(k + l) * comb(n, l) / 2**(n - l)
    return K


def T3(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for k in range(n + 1):
        for l in range(n + 1):
            sum = 0
            for j in range(n + 1):
                sum += comb(l, j) * comb(n - l, n - k - j) * (-1)**j
            K[k, l] = sum * comb(n, l)
    return K * 2**-n


def iT3(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for k in range(n + 1):
        for l in range(n + 1):
            sum = 0
            for j in range(n + 1):
                sum += comb(n - l, j) * comb(l, k - j) * (-1)**j
            K[k, l] = sum / comb(n, k)
    return K
