from typing import Tuple
import numpy as np
from . import matrices


def single_shot_estimators(n: int) -> Tuple[np.ndarray]:
    """
    Generate $n$-qubit single-shot estimators for the quantum weight 
    distributions a, b, a', b', a'', and b''. 

    Parameters
    ----------
    n : int
        Number of qubits

    Returns
    -------
    Tuple[np.ndarray]
        A tuple of 6 matrices for a, b, a', b', a'', and b'', respectively. 
        Each matrix consists of $n+1$ estimators as columns where the column 
        index corresponds to the number of measured singlets. 
    """
    M2 = matrices.M2(n)
    iT2 = matrices.iT2(n)
    iT3 = matrices.iT3(n)
    return iT2, iT2 @ M2, iT3, np.flipud(iT3), np.eye(n + 1), M2
