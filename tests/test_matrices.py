import unittest
import numpy as np
from src.qsalto import *
from scipy.special import comb


class TestData(unittest.TestCase):

    def test_inverse(self):
        for n in range(1, 12):
            np.testing.assert_almost_equal(np.linalg.inv(M(n)), M(n))
            np.testing.assert_almost_equal(np.linalg.inv(M1(n)), M1(n))
            np.testing.assert_almost_equal(np.linalg.inv(M2(n)), M2(n))
            np.testing.assert_almost_equal(np.linalg.inv(T1(n)), iT1(n))
            np.testing.assert_almost_equal(np.linalg.inv(T2(n)), iT2(n))
            np.testing.assert_almost_equal(np.linalg.inv(T3(n)), iT3(n))

    def test_chaining(self):
        for n in range(1, 30):
            np.testing.assert_almost_equal(T3(n) @ T1(n), T2(n))
            np.testing.assert_almost_equal(iT1(n) @ iT3(n), iT2(n))
            np.testing.assert_almost_equal(T1(n) @ iT2(n), iT3(n))
            np.testing.assert_almost_equal(T2(n) @ iT1(n), T3(n))

    def test_M1_identity(self):
        for n in range(1, 30):
            np.testing.assert_almost_equal(T1(n) @ M(n) @ iT1(n), M1(n))

    def test_M2_identity(self):
        for n in range(1, 30):
            np.testing.assert_almost_equal(T2(n) @ M(n) @ iT2(n), M2(n))

    def test_separable(self):
        for n in range(2, 20):
            apd = np.full(n + 1, 1)
            sld = iT1(n) @ apd
            np.testing.assert_equal(sld, comb(n, np.arange(n+1)) / 2**n)

            tpd = T3(n) @ apd
            np.testing.assert_almost_equal(tpd[n], 1)
            np.testing.assert_almost_equal(tpd[:n], np.zeros(n))

    def test_ghz(self):
        for n in range(2, 30, 2):
            apd = np.full(n + 1, .5)
            apd[[0, n]] = 1

            sld = iT1(n) @ apd
            ks = np.arange(n+1)
            ghz_sld = comb(n, ks) * (1+(-1)**ks) / 2
            ghz_sld[n] += 2**(n-1)
            ghz_sld /= 2**n
            np.testing.assert_equal(sld, ghz_sld)

            tpd = T3(n) @ apd
            np.testing.assert_almost_equal(tpd, ghz_sld)

    def test_single_entry(self):
        for t in [M, M1, M2, T1, iT1, T2, iT2, T3, iT3]:
            with self.subTest("", t=t):
                n = 11
                matrix = t(n)
                for i in range(n + 1):
                    for j in range(n + 1):
                        val = t(n, entry=[i, j])
                        np.testing.assert_allclose(matrix[i, j], val)
