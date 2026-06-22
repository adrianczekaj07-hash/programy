import unittest
import TestKlasse1
import TestKlasse2

loader = unittest.TestLoader()
suite  = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(TestKlasse1))
suite.addTests(loader.loadTestsFromModule(TestKlasse2))
runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
