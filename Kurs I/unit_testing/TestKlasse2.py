import unittest
import random as r
class TestKlasse2(unittest.TestCase):
    def test_1(self):
        a = set(range(1,6))
        b = set(range(1,6))
        self.assertSetEqual(a, b)

