import unittest
import test_12_3

raceST = unittest.TestSuite()
raceST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
raceST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(raceST)


