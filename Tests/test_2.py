import unittest 
import context
import Finstein.finhyp as finhyp

class Tests(unittest.TestCase):

    def test_ztest(self):
        actual= finhyp.ztest(641,600,100,20)
        expected= [round(1.834,3),round(0.0334,4),True]
        self.assertListEqual(actual,expected,"ztest() failed")

    def test_ztest2(self):
        actual= finhyp.ztest2(641,613.3,10,100,90,20,20)
        expected= [round(0.588,3),round(0.2781,4),False]
        self.assertListEqual(actual,expected,"ztest2() failed")

    def test_ztestp(self):
        actual= finhyp.ztestp(0.32,0.46,0.39,0,200,200)
        expected= [round(-2.8703,3),round(0.00205,4),True]
        self.assertListEqual(actual,expected,"ztestp() failed")

    def test_ttest(self):
        actual = finhyp.ttest(606.8,600,13.14,10)
        expected= [round(1.636,3),round(0.06810,4),True]
        self.assertListEqual(actual,expected,"ttest() failed")

    

    def test_ttest2(self):
        actual = finhyp.ttest2(16.85,15.79,0,4.31,4.97,65,75,V=True)
        expected= [round(1.3381,3),round(0.0916,4),False]
        self.assertListEqual(actual,expected,"ttest2() failed")
        
        




if __name__ == '__main__': 
    unittest.main() 