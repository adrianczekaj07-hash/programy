import unittest
import random as r
class SubTests(unittest.TestCase):


    def test_mehrfach(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertNotEqual(i, 5)


if __name__ == '__main__':
    unittest.main()
