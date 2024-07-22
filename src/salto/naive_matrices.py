
import numpy as np
from scipy.special import comb as scomb


def comb(n, k):
    return scomb(n, k, exact=True)



def M(n: int, entry=None) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            sum = 0
            for l in range(n + 1):
                sum += comb(n - j, i - l) * comb(j, l) * (-1)**l * 3**(i - l)
            K[i, j] = sum
    K *= 2**-n
    return K


def M1(n: int) -> np.ndarray:
    return np.fliplr(np.eye(n+1))


def M2(n: int) -> np.ndarray:
    return np.diag(np.resize([1, -1], n+1)[::-1])


def T2(n: int) -> np.ndarray:
    K = M(n)
    for col in range(1, n + 1, 2):
        K[:, col] *= -1.
    return K


def iT2(n: int) -> np.ndarray:
    K = M(n)
    for row in range(1, n + 1, 2):
        K[row] *= -1.
    return K


def T1(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            K[i, j] = comb(n - j, n - i) * 2**(n - i) / comb(n, i)
    return K


def iT1(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            K[i, j] = comb(n - j, i - j) * (-1)**(i + j) * comb(n, j) / 2**(n - j)
    return K


def T3(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            sum = 0
            for l in range(n + 1):
                sum += comb(n - j, i - l) * comb(j, l) * (-1)**(j - l)
            K[i, j] = sum * comb(n, j)
    return K * 2**-n


def iT3(n: int) -> np.ndarray:
    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            sum = 0
            for l in range(n + 1):
                sum += comb(n - j, i - l) * comb(j, l) * (-1)**(i - l)
            K[i, j] = sum / comb(n, i)
    return K
