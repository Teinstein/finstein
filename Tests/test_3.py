import unittest 
import context
import Finstein.finspot as finspot

class Tests(unittest.TestCase):

    def test_IR(self):
        spot =[0.05,0.06,0.07,0.085,0.10,0.11]
        actual = finspot.IR(spot)
        expected = 0.11
        self.assertAlmostEqual(actual,expected,2,"IR() failed")



    def test_FR(self): #Test for forward rate
        spot =[0.05,0.06,0.07,0.085,0.10,0.11]

        actual = finspot.FR(spot,4)
        expected = 0.35 
        self.assertAlmostEqual(actual,expected,2,"FR() failed")


if __name__ == '__main__': 
    unittest.main() 
