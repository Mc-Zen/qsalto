""" 
qsalto
======

Provides transformations between several (normalized) quantum weight enumerators, including
- Shor-Laflamme enumerators a, b,
- Rains unitary enumerators a', b',
- and Rains shadow enumerators a''.

"""

from .matrices import M, M1, M2, T1, iT1, T2, iT2, T3, iT3
from .single_shot import single_shot_estimators
