
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


def M(n: int, entry: tuple | None = None) -> np.ndarray:
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

    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            sum = 0
            for l in range(n + 1):
                sum += comb(n - j, i - l) * comb(j, l) * (-1)**l * 3**(i - l)
            K[i, j] = sum
    K /= 2**n
    return K


def M1(n: int, entry: tuple | None = None) -> np.ndarray:
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


def M2(n: int, entry: tuple | None = None) -> np.ndarray:
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


def T2(n: int, entry: tuple | None = None) -> np.ndarray:
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


def iT2(n: int, entry: tuple | None = None) -> np.ndarray:
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


def T1(n: int, entry: tuple | None = None) -> np.ndarray:
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

    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            K[i, j] = comb(n - j, n - i) * 2**(n - i) / comb(n, i)
    return K


def iT1(n: int, entry: tuple | None = None) -> np.ndarray:
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

    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            K[i, j] = comb(n - j, i - j) * (-1)**(i + j) * comb(n, j) / 2**(n - j)
    return K


def T3(n: int, entry: tuple | None = None) -> np.ndarray:
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

    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            sum = 0
            for l in range(n + 1):
                sum += comb(n - j, i - l) * comb(j, l) * (-1)**(j - l)
            K[i, j] = sum * comb(n, j)
    return K * 2**-n


def iT3(n: int, entry: tuple | None = None) -> np.ndarray:
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

    K = np.zeros([n + 1, n + 1])
    for i in range(n + 1):
        for j in range(n + 1):
            sum = 0
            for l in range(n + 1):
                sum += comb(n - j, i - l) * comb(j, l) * (-1)**(i - l)
            K[i, j] = sum / comb(n, i)
    return K
