import unittest as ut
import zutesten2
class TestKlasse(ut.TestCase):
   def test_gerade(self):
      m = zutesten2.geradezahlen(100)
      print(m)
      ok=0
      nichtok = 0
      for i in m:
         try:
            self.assertEqual(i%2,0)
            ok += 1
         except:
            nichtok += 1
      print("Fehler: ", nichtok)



if __name__ == '__main__':
   ut.main()
