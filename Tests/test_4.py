import unittest 
import context
import Finstein.finbsm as finbsm

class Tests(unittest.TestCase):

    def test_bsm_put(self):
        actual = finbsm.bsm(50, 100, 1, 0.05, 0.25,"put")
        expected = 45.15029
        self.assertAlmostEqual(actual,expected,2,"bsm() put failed")

    def test_bsm_call(self):
        actual = finbsm.bsm(50, 100, 1, 0.05, 0.25,"call")
        expected = 0.02735
        self.assertAlmostEqual(actual,expected,2,"bsm() call failed")

    def test_bsm_div_put(self):
        actual = finbsm.bsm_div(300, 250, 1, 0.03, 0.05,0.15,"put")
        expected = 2.80
        self.assertAlmostEqual(actual,expected,2,"bsm_div() put failed")
        
    def test_bsm_div_call(self):
        actual = finbsm.bsm_div(300, 250, 1, 0.03, 0.05,0.15,"call")
        expected = 45.56
        self.assertAlmostEqual(actual,expected,2,"bsm_div() call failed")

if __name__ == '__main__': 
    unittest.main() 

