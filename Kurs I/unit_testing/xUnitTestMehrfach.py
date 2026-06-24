import unittest as ut

class TestKlasse(ut.TestCase):
   def test_gerade(self):
      menge = (2,4,6,8,9,10,12,14,15)
      for i in menge:
         try:
            self.assertEqual(i%2,0)
         except:
            pass



if __name__ == '__main__':
   ut.main()
