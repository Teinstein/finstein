import math
from scipy.stats import norm,t

def ztest(X:float, mu:float, sd:float,n:float,alpha=0.05,two_tail=False):

  """ztest(): Calculates Z test for single sample, two tailed as well as single.

  :param X: Sample mean
  :type X: float
  :param mu: Population mean/ Data mean
  :type mu: float
  :param sd: Standard Deviation
  :type sd: float
  :param n: Sample size
  :type n: float
  :param alpha: P value Limit/Significance value (default:0.05)
  :type alpha: float
  :param two_tail: Enter true for conducting two-tailed test. (default: False)
  :type two_tail: Boolean 
  :return: [Z value, Pvalue, True/False (Test was conclusive or not)]
  :rtype: list
  """
  tail=1

  if(two_tail):
    tail=2
  if(sd==0 or n==0):
    return None
  z=(X-mu)/(sd/(math.sqrt(n)))
  pval=tail*(norm.sf(abs(z)))

  return round(z, 3), round(pval, 4)

def ztest2(X1:float, X2:float, mudiff:float, sd1:float, sd2:float, n1:float, n2:float,alpha=0.05,two_tail=False):
  """ztest2(): Calculates Z test for two sampled data, two tailed as well as single.

  :param X1: Sample mean 1
  :type X: float
  :param X2: Sample mean 2
  :type X: float
  :param mudiff: mean difference
  :type mu: float
  :param sd1: Standard Deviation 1
  :type sd1: float
  :param sd2: Standard Deviation 2
  :type sd2: float
  :param n1: Sample size 1
  :type n1: float
  :param n2: Sample size 2
  :type n2: float
  :param alpha: P value Limit/Significance value (default:0.05)
  :type alpha: float
  :param two_tail: Enter true for conducting two-tailed test. (default: False)
  :type two_tail: Boolean 
  :return: [Z score, P value, True/False (Test was conclusive or not)]
  :rtype: list
  """

  tail=1
  if(two_tail):
    tail=2

  if(n1+n2<=0):
    return None

  pooledSE = math.sqrt(sd1**2/n1 + sd2**2/n2)
  if (pooledSE==0):
    return None
  z = ((X1 - X2) - mudiff)/pooledSE
  pval = tail*norm.sf(abs(z))
  return round(z, 3), round(pval, 4)

def ttest(X:float, n:float, mu:float, sd:float, alpha=0.5,two_tail=False):
  """ttest(): Calculates T test for single sample, two tailed as well as single.

  :param X: Sample mean
  :type X: float
  :param mu: Population mean/ Data mean
  :type mu: float
  :param sd: Standard Deviation
  :type sd: float
  :param n: Sample size
  :type n: float
  :param alpha: P value Limit/Significance value (default:0.05)
  :type alpha: float
  :param two_tail: Enter true for conducting two-tailed test. (default: False)
  :type two_tail: Boolean 
  :return: [T score, P value, True/False (Test was conclusive or not)]
  :rtype: list
  """
  tail=1
  if(two_tail):
    tail=2
  if(sd==0 or n==0):
    return None

  tt=(X-mu)/(sd/((n)**0.5))
  pval=tail*(t.sf(abs(tt),n-1))
  return round(tt, 3), round(pval, 4)

def ttest2(X1:float, X2:float, mudiff:float, sd1:float, sd2:float, n1:float, n2:float,two_tail=False):
  """ttest2(): Calculates T test for two sampled data (independent), two tailed as well as single.

  :param X1: Sample mean 1
  :type X: float
  :param X2: Sample mean 2
  :type X: float
  :param mudiff: mean difference
  :type mu: float
  :param sd1: Standard Deviation 1
  :type sd1: float
  :param sd2: Standard Deviation 2
  :type sd2: float
  :param n1: Sample size 1
  :type n1: float
  :param n2: Sample size 2
  :type n2: float
  :param alpha: P value Limit/Significance value (default:0.05)
  :type alpha: float
  :param two_tail: Enter true for conducting two-tailed test. (default: False)
  :type two_tail: Boolean 
  :return: [T score, P value, True/False (Test was conclusive or not)]
  :rtype: list
  """
  tail=1
  if(two_tail):
    tail=2
  if(n1+n2<=0):
    return None
  pooledSE = math.sqrt((((sd1**2)*(n1-1) +(sd2**2)*(n2-2))/(n1+n2-2))*math.sqrt(1/n1 + 1/n2))
  if (pooledSE==0):
    return None
  tt = ((X1 - X2) - mudiff)/pooledSE
  pval = tail*(t.sf(abs(tt),n1+n2-2))

  return round(tt, 3), round(pval, 4)


