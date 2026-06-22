import unittest
import random as r
class TestKlasse1(unittest.TestCase):
    def test_1(self):
        a = r.sample(range(1,6),5)
        b = r.sample(range(1,6),5)

        self.assertListEqual(a, b)

