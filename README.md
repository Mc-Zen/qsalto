

![](docs/media/logo.svg)

_transform your quantum weight enumerators_



[![PyPI Package](https://img.shields.io/pypi/v/qsalto)](https://pypi.org/project/qsalto/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/Mc-Zen/qsalto/blob/main/LICENSE)
[![Tests](https://github.com/Mc-Zen/qsalto/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Mc-Zen/qsalto/actions/workflows/run-tests.yml)
---



**qsalto** provides transformations between several quantum weight enumerators, including
- Shor-Laflamme enumerators,
- Rains shadow enumerators,
- Rains unitary enumerators,
- and averaged subsystem purities. 


We provide both 
- a python package, (soon) available on PyPi: https://pypi.org/project/qsalto,
- a web viewer for visualizing the transformation matrices at https://mc-zen.github.io/qsalto.


## Python package

The python package `qsalto` can be installed via `pip install qsalto` and features functions to generate nine classes of transformation matrices. 


|Matrix | Function | Transforms from ... | ... to | Self-inverse |
|-------|----------|------|---|--|
|$M$    |`M(n)`    |$\mathbf{a}$ |$\mathbf{b}$ |✅|
|$M'$    |`M1(n)`    |$\mathbf{a'}$ |$\mathbf{b'}$ |✅|
|$M''$    |`M2(n)`    |$\mathbf{a''}$ |$\mathbf{b''}$ |✅|
|$T'$    |`T1(n)`    |$\mathbf{a}$, $\mathbf{b}$ |$\mathbf{a'}$, $\mathbf{b'}$ |❎|
|$T'^{-1}$    |`iT1(n)`    |$\mathbf{a'}$, $\mathbf{b'}$ |$\mathbf{a}$, $\mathbf{b}$ |❎|
|$T''$    |`T2(n)`    |$\mathbf{a}$, $\mathbf{b}$ |$\mathbf{a''}$, $\mathbf{b''}$ |❎|
|$T''^{-1}$    |`iT2(n)`    |$\mathbf{a''}$, $\mathbf{b''}$ |$\mathbf{a}$, $\mathbf{b}$ |❎|
|$T'''$    |`T3(n)`    |$\mathbf{a'}$, $\mathbf{b'}$ |$\mathbf{a''}$, $\mathbf{b''}$ |❎|
|$T'''^{-1}$    |`iT3(n)`    |$\mathbf{a''}$, $\mathbf{b''}$ |$\mathbf{a'}$, $\mathbf{b'}$ |❎|



<!-- ❌✔️ -->

## License

This library is distributed under the MIT License.

If you want to support work like this, please cite our paper: tba
