import unittest
import random as r


class TestLottoZiehung(unittest.TestCase):

    def test_mehrfach(self):
        liste = Lotto.ziehung(self)
        for i in range(0,len(liste)-1):
            self.assertNotIn(i, liste)


class Lotto:
    def ziehung(self):
        r.seed()
        verfuegbareZahlen = list(range(1,49))
        return r.sample(verfuegbareZahlen, 6)
if __name__ == '__main__':
    unittest.main()
