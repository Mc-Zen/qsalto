
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/Mc-Zen/qsalto/raw/main/docs/media/logo.svg">
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Mc-Zen/qsalto/raw/main/docs/media/logo-dark.svg">
  <img alt="qsalto logo" src="https://github.com/Mc-Zen/qsalto/raw/main/docs/media/logo.svg">
</picture>


_transform your quantum weight enumerators_



[![PyPI Package](https://img.shields.io/pypi/v/qsalto)](https://pypi.org/project/qsalto/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/Mc-Zen/qsalto/blob/main/LICENSE)
[![Tests](https://github.com/Mc-Zen/qsalto/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Mc-Zen/qsalto/actions/workflows/run-tests.yml)
---



**qsalto** provides transformations between several (normalized) quantum weight enumerators, including
- Shor-Laflamme enumerators[^1] $a$, $b$,
- Rains unitary enumerators[^2] $a'$, $b'$,
- and Rains shadow enumerators[^3] $a''$.


We provide both 
- a python package, available on PyPI: https://pypi.org/project/qsalto,
- a web viewer for visualizing the transformation matrices at https://mc-zen.github.io/qsalto.


<img src="https://github.com/Mc-Zen/qsalto/raw/main/docs/media/transformation-diagram.svg" width="420">

## Python package

The python package `qsalto` can be installed via `pip install qsalto` and features functions to generate nine classes of transformation matrices. 


|Matrix     | Function | Transforms from ...           | ... to                        |is self-inverse|
|-----------|----------|-------------------------------|-------------------------------|---------------|
|$M$        |`M(n)`    |$\mathbf{a}$                   |$\mathbf{b}$                   |✅            |
|$M'$       |`M1(n)`   |$\mathbf{a'}$                  |$\mathbf{b'}$                  |✅            |
|$M''$      |`M2(n)`   |$\mathbf{a''}$                 |$\mathbf{b''}$                 |✅            |
|$T'$       |`T1(n)`   |$\mathbf{a}$, $\mathbf{b}$     |$\mathbf{a'}$, $\mathbf{b'}$   |❌            |
|$T'^{-1}$  |`iT1(n)`  |$\mathbf{a'}$, $\mathbf{b'}$   |$\mathbf{a}$, $\mathbf{b}$     |❌            |
|$T''$      |`T2(n)`   |$\mathbf{a}$, $\mathbf{b}$     |$\mathbf{a''}$, $\mathbf{b''}$ |❌            |
|$T''^{-1}$ |`iT2(n)`  |$\mathbf{a''}$, $\mathbf{b''}$ |$\mathbf{a}$, $\mathbf{b}$     |❌            |
|$T'''$     |`T3(n)`   |$\mathbf{a'}$, $\mathbf{b'}$   |$\mathbf{a''}$, $\mathbf{b''}$ |❌            |
|$T'''^{-1}$|`iT3(n)`  |$\mathbf{a''}$, $\mathbf{b''}$ |$\mathbf{a'}$, $\mathbf{b'}$   |❌            |

To compute the full matrices, an optimized algorithm making use of recursive patterns is employed. Each matrix generator also features the computation of single elements through, e.g., `M(100, entry=[3,4])` where `entry` specifies the row and column of the entry (in that order). 

### Single-shot estimators

Furthermore, the function `single_shot_estimators(n)` generates single-shot estimators for $a$, $b$, $a'$, $b'$, $a''$, and $b''$ for all possible numbers $m=0,...,n$ of singlets as an outcome of a two-copy Bell measurement. This function returns six 2D-arrays (one for each quantum weight enumerator in the order as given above) with the estimator for $m$ singlets in the $m$-th column. 

### High-precision transformation matrices

For some applications, a higher precision than 64 bit floating point is needed for the transformation matrices. For this purpose, each transformation features a `precise` argument (which defaults to `false`). If set to `true`, an `mpmath.matrix` is returned instead of an `np.array`. This requires [`mpmath`](https://mpmath.org/) to be installed. The precision can for example be set via `mpmath.mp.dps = 120` (more on precision with mpmath, see [here](https://mpmath.org/doc/current/basics.html#setting-the-precision)) before calling the transformation generator. 


## License

This library is distributed under the MIT License.

If you want to support work like this, please cite our paper: tba



[^1]: [P. Shor and R. Laflamme, Phys. Rev. Lett. **78**, 1600 (1997)](http://dx.doi.org/10.1103/PhysRevLett.78.1600)

[^2]: [E. M. Rains, IEEE Trans. Inf. Th., **44**, 1388 (1998)](http://dx.doi.org/10.1109/18.681316)

[^3]: [E. M. Rains, IEEE Trans Inf. Th. **45**, 2361 (1999)](http://dx.doi.org/10.1109/18.796376)


