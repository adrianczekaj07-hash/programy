import unittest as ut

class TestKlasse(ut.TestCase):
   def test_1(self):
      self.assertEqual(2%2,0)

   def test_2(self):
      self.assertNotEqual(2%2,0)
      
   def test_3(self,i):
      self.assertEqual(i%2,0)


if __name__ == '__main__':
    i = 0
    nichtok=0
    while i < 10:
        try:
            TestKlasse().test_3(i)
        except:
            nichtok+=1
        i += 1
    print(nichtok)
  #ut.main()
    
  
