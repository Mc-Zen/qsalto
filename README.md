
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



**qsalto** provides transformations between several quantum weight enumerators, including
- Shor-Laflamme enumerators $a$, $b$,
- Rains unitary enumerators $a'$,
- and Rains shadow enumerators $a''$.


We provide both 
- a python package, available on PyPi: https://pypi.org/project/qsalto,
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

To compute the full matrices, a special algorithm making use of recursive patterns is employed. Each matrix generator also features the computation of single elements through, e.g., `M(100, entry=[3,4])` where `entry` specifies the row and column of the entry (in that order). This is only faster than computing the entire matrix when merely very few entries are computed. 

### Single-shot estimators

Furthermore, the function `single_shot_estimators(n)` generates single-shot estimators for $a$, $b$, $a'$, $b'$, $a''$, and $b''$ for all possible numbers $m=0,...,n$ of singlets as an outcome of a two-copy bell measurement. This function returns six 2D-arrays (one for each quantum weight enumerator in the order as given above) with the estimator for $m$ singlets in the $m$-th column. 



## License

This library is distributed under the MIT License.

If you want to support work like this, please cite our paper: tba
