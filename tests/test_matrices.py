import unittest
import numpy as np
from src.salto import *


class TestData(unittest.TestCase):

    def test_inverse(self):
        np.testing.assert_almost_equal(np.linalg.inv(M(10)), M(10))
        np.testing.assert_almost_equal(np.linalg.inv(M1(10)), M1(10))
        np.testing.assert_almost_equal(np.linalg.inv(M2(10)), M2(10))
        np.testing.assert_almost_equal(np.linalg.inv(T1(10)), iT1(10))
        np.testing.assert_almost_equal(np.linalg.inv(T2(10)), iT2(10))
        np.testing.assert_almost_equal(np.linalg.inv(T3(10)), iT3(10))
