
import numpy as np
from scipy.special import comb as scomb
from . import single_entry


def comb(n, k):
    return scomb(n, k, exact=True)


def assert_valid_entry(entry, n):
    assert hasattr(entry, '__getitem__') and len(
        entry) == 2, f"Invalid entry `{entry}`. Entry should be a pair of integers"
    assert 0 <= entry[0] <= n and 0 <= entry[
        1] <= n, f"Matrix entry `{entry}` out of range ({n=})"


def M(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Self-inverse transformation matrix between Shor-Laflamme distributions $a$ and $b$.

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.M(n, *entry)

    K = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(0, n + 1):
        K[0][k] = 1
        K[k][-1] = comb(n, k) * (-1)**k
    for k in range(1, n + 1):
        for l in reversed(range(n)):
            K[k][l] = 3 * K[k - 1][l + 1] + K[k - 1][l] + K[k][l + 1]
    for k in range(n + 1):
        for l in range(n + 1):
            K[k][l] /= 2**n
    K = np.array(K, dtype=float)
    return K


def M1(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Self-inverse transformation matrix between quantum weight enumerators $a'$ and $b'$.

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.M1(n, *entry)

    return np.fliplr(np.eye(n+1))


def M2(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Self-inverse transformation matrix between quantum weight enumerators $a''$ and $b''$.

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.M2(n, *entry)

    return np.diag(np.resize([1, -1], n+1)[::-1])


def T2(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Transformation matrix from Shor-Laflamme enumerators $a$ to Rains shadow enumerators $a''$. 

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.T2(n, *entry)

    K = M(n)
    for col in range(1, n + 1, 2):
        K[:, col] *= -1.
    return K


def iT2(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Transformation matrix from Rains shadow enumerators $a''$ to Shor-Laflamme enumerators $a$. 

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.iT2(n, *entry)

    K = M(n)
    for row in range(1, n + 1, 2):
        K[row] *= -1.
    return K


def T1(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Transformation matrix from Shor-Laflamme enumerators $a$ to Rains unitary enumerators $a'$. 

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.T1(n, *entry)

    K = [[0] * (n + 1) for _ in range(n + 1)]

    for k in range(n + 1):
        K[k][k] = 1
        K[-1][k] = 1
    for l in reversed(range(0, n)):
        for k in range(l - 1, n):
            K[k][l] = K[k][l + 1] + K[k + 1][l + 1]
    K = np.array(K, dtype=float)
    for k in range(n + 1):
        K[k] *= 2**(n - k) / K[k, 0]
    return K


def iT1(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Transformation matrix from Rains unitary enumerators $a'$ to Shor-Laflamme enumerators $a$. 

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.iT1(n, *entry)

    K = [[0] * (n+1) for _ in range(n + 1)]

    for k in range(n + 1):
        K[k][k] = 1
        K[-1][k] = 1
    for l in reversed(range(0, n)):
        for k in range(l - 1, n):
            K[k][l] = K[k][l + 1] + K[k + 1][l + 1]
    K = np.array(K, dtype=float)
    for l in reversed(range(n + 1)):
        K[:, l] *= K[l, 0] / 2**(n - l)
    for l in range(n + 1):
        for k in range(l + 1, n + 1, 2):
            K[k, l] *= -1
    return K


def T3(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Transformation matrix from Rains' unitary enumerators $a'$ to Rains' shadow enumerators $a''$. 

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.T3(n, *entry)

    K = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(0, n + 1):
        K[0][k] = (-1)**k
        K[k][0] = comb(n, k)
    for k in range(1, n + 1):
        for l in range(1, n + 1):
            K[k][l] = K[k - 1][l - 1] - K[k - 1][l] - K[k][l - 1]
    K = np.array(K, dtype=float)
    for l in range(n + 1):
        K[:, l] *= np.abs(K[l, 0])
    return K * 2**-n


def iT3(n: int, entry: tuple | None = None) -> np.ndarray | float:
    """Transformation matrix from Rains' shadow enumerators $a''$ to Rains' unitary enumerators $a'$. 

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    np.ndarray
        $(n+1)×(n+1)$ matrix.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return single_entry.iT3(n, *entry)

    K = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(0, n + 1):
        K[0][k] = 1
        K[k][0] = comb(n, k) * (-1)**k
    for k in range(1, n + 1):
        for l in range(1, n + 1):
            K[k][l] = K[k - 1][l - 1] + K[k - 1][l] + K[k][l - 1]
    K = np.array(K, dtype=float)
    for k in range(n + 1):
        K[k] *= 1 / np.abs(K[k, 0])
    return K
