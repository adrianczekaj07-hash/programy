import unittest as ut
import zutesten1
class TestKlasse(ut.TestCase):
   def test_gerade(self):
      self.assertLess(zutesten1.zahlen(),0.5)



if __name__ == '__main__':
   ut.main()
