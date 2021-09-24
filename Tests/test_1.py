import unittest 
import context
import Finstein.fincalc as fincalc


class Tests(unittest.TestCase):
    def test_FV(self):
        actual= fincalc.FV(13000,0.08,6,1)
        expected= 20629.37
        self.assertAlmostEqual(actual,expected,2,"FV() failed")
    def test_PV(self):
        actual= fincalc.PV(100,0.05,0.06,5,1)
        expected = 95.7867
        self.assertAlmostEqual(actual,expected,2,"PV() failed")
    def test_solve(self):
        #test to find n given pv,fv,r and m.
        actual= fincalc.solve(fv=29703,pv=9000,r=0.12,m=12)
        expected = 10.000
        self.assertAlmostEqual(actual,expected,2,"solve() failed")


if __name__ == '__main__': 
    unittest.main() 
