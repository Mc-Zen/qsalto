
import numpy as np
from scipy.special import comb as scomb
from typing import Union, overload
from . import single_entry
from . import single_entry_precise

try:
    import mpmath as mp
except ImportError:
    import mp_not_available
    mp = mp_not_available.mp_error()

def get_single_entry(precise):
    return single_entry_precise if precise else single_entry

def comb(n, k):
    return scomb(n, k, exact=True)


def assert_valid_entry(entry, n):
    assert hasattr(entry, '__getitem__') and len(
        entry) == 2, f"Invalid entry `{entry}`. Entry should be a pair of integers"
    assert 0 <= entry[0] <= n and 0 <= entry[
        1] <= n, f"Matrix entry `{entry}` out of range (n={n})"


@overload
def M(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def M(n: int, entry: tuple, precise=False) -> float: ...

@overload
def M1(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def M1(n: int, entry: tuple, precise=False) -> float: ...

@overload
def M2(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def M2(n: int, entry: tuple, precise=False) -> float: ...

@overload
def T1(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def T1(n: int, entry: tuple, precise=False) -> float: ...
@overload
def iT1(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def iT1(n: int, entry: tuple, precise=False) -> float: ...

@overload
def T2(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def T2(n: int, entry: tuple, precise=False) -> float: ...
@overload
def iT2(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def iT2(n: int, entry: tuple, precise=False) -> float: ...

@overload
def T3(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def T3(n: int, entry: tuple, precise=False) -> float: ...
@overload
def iT3(n: int, entry: None = None, precise=False) -> np.ndarray: ...
@overload
def iT3(n: int, entry: tuple, precise=False) -> float: ...


def M(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Self-inverse transformation matrix between Shor-Laflamme distributions $a$ and $b$.

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 
        
    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).M(n, *entry)

    K = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(0, n + 1):
        K[0][k] = 1
        K[k][-1] = comb(n, k) * (-1)**k
    for k in range(1, n + 1):
        for l in reversed(range(n)):
            K[k][l] = 3 * K[k - 1][l + 1] + K[k - 1][l] + K[k][l + 1]
    if precise:
        return mp.matrix(K) / 2**n
    else:
        for k in range(n + 1):
            for l in range(n + 1):
                K[k][l] /= 2**n
        K = np.array(K, dtype=float)
        return K


def M1(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Self-inverse transformation matrix between quantum weight enumerators $a'$ and $b'$.

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 

    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).M1(n, *entry)

    if precise:
        K = mp.matrix(n + 1)
        for i in range(n + 1):
            K[i, n - i] = 1
        return K
    else:
        return np.fliplr(np.eye(n + 1))


def M2(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Self-inverse transformation matrix between quantum weight enumerators $a''$ and $b''$.

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 

    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).M2(n, *entry)

    if precise:
        K = mp.eye(n + 1)
        for i in range(1, n + 1, 2):
            K[n - i, n - i] = -1
        return K
    else:
        return np.diag(np.resize([1, -1], n+1)[::-1])


def T2(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Transformation matrix from Shor-Laflamme enumerators $a$ to Rains shadow enumerators $a''$. 

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 

    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).T2(n, *entry)

    K = M(n, precise=precise)
    for col in range(1, n + 1, 2):
        K[:, col] *= -1.
    return K


def iT2(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Transformation matrix from Rains shadow enumerators $a''$ to Shor-Laflamme enumerators $a$. 

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 

    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).iT2(n, *entry)

    K = M(n, precise=precise)
    for row in range(1, n + 1, 2):
        K[row, :] *= -1.
    return K


def T1(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Transformation matrix from Shor-Laflamme enumerators $a$ to Rains unitary enumerators $a'$. 

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 

    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).T1(n, *entry)

    K = [[0] * (n + 1) for _ in range(n + 1)]

    for k in range(n + 1):
        K[k][k] = 1
        K[-1][k] = 1
    for l in reversed(range(0, n)):
        for k in range(l - 1, n):
            K[k][l] = K[k][l + 1] + K[k + 1][l + 1]
    if precise:
        K = mp.matrix(K)
    else:
        K = np.array(K, dtype=float)

    for k in range(n + 1):
        K[k, :] *= 2**(n - k) / K[k, 0]
    return K


def iT1(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Transformation matrix from Rains unitary enumerators $a'$ to Shor-Laflamme enumerators $a$. 

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 

    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).iT1(n, *entry)

    K = [[0] * (n+1) for _ in range(n + 1)]

    for k in range(n + 1):
        K[k][k] = 1
        K[-1][k] = 1
    for l in reversed(range(0, n)):
        for k in range(l - 1, n):
            K[k][l] = K[k][l + 1] + K[k + 1][l + 1]
    if precise:
        K = mp.matrix(K)
    else:
        K = np.array(K, dtype=float)

    for l in reversed(range(n + 1)):
        K[:, l] *= K[l, 0] / 2**(n - l)
    for l in range(n + 1):
        for k in range(l + 1, n + 1, 2):
            K[k, l] *= -1
    return K


def T3(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Transformation matrix from Rains' unitary enumerators $a'$ to Rains' shadow enumerators $a''$. 

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 

    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).T3(n, *entry)

    K = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(0, n + 1):
        K[0][k] = (-1)**k
        K[k][0] = comb(n, k)
    for k in range(1, n + 1):
        for l in range(1, n + 1):
            K[k][l] = K[k - 1][l - 1] - K[k - 1][l] - K[k][l - 1]

    if precise:
        K = mp.matrix(K)
    else:
        K = np.array(K, dtype=float)

    for l in range(n + 1):
        K[:, l] *= np.abs(K[l, 0])
    return K / 2**n


def iT3(n: int, entry: Union[tuple, None] = None, precise=False) -> Union[np.ndarray, float]:
    """Transformation matrix from Rains' shadow enumerators $a''$ to Rains' unitary enumerators $a'$. 

    Parameters
    ----------
    n : int
        Number of qubits
    entry : Tuple[int, int] | None
        If given, only the entry specified by these indices is computed and returned. 
    precise : bool
        If `true`, an `mp.matrix` returned, using current `mpmath` precision. 

    Returns
    -------
    np.ndarray | float
        $(n+1)×(n+1)$ matrix or single entry.
    """
    if entry is not None:
        assert_valid_entry(entry, n)
        return get_single_entry(precise).iT3(n, *entry)

    K = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(0, n + 1):
        K[0][k] = 1
        K[k][0] = comb(n, k) * (-1)**k
    for k in range(1, n + 1):
        for l in range(1, n + 1):
            K[k][l] = K[k - 1][l - 1] + K[k - 1][l] + K[k][l - 1]

    if precise:
        K = mp.matrix(K)
    else:
        K = np.array(K, dtype=float)

    for k in range(n + 1):
        K[k, :] *= 1 / np.abs(K[k, 0])
    return K
