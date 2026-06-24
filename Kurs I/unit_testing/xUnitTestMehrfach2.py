import unittest as ut

class TestKlasse(ut.TestCase):
   def test_gerade(self):
      self.assertEqual(2%2,0)



if __name__ == '__main__':
   i = 0
   while i < 10:
      ut.main()
      i += 1
