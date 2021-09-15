import math 
'''
FV()
paramaters: 

pv = Present Value
r = Rate of Interest/Discount Rate (in decimals eg: 0.05 for 5%)
n = Number of Years
m = Frequency of Interest Calculation (eg: 2 for Semi-annually)

'''
#Calculation of Future Value given pv,r,m,n
def FV(pv:float,r:float,n:float,m=1):
  if(m<=0):return None
  return pv*((1+r/m)**(m*n))


'''
PV()
paramaters: 

fv = Future Value
c = coupon rate (in decimals eg: 0.05 for 5%)
r = Rate of Interest/Discount Rate (in decimals eg: 0.05 for 5%)
n = Number of Years
m = Frequency of Interest Calculation (eg: 2 for Semi-annually)

'''

#Calculation of Present Value given fv,c,r,m,n
def PV(fv:float,c:float,r:float,n:float,m=1):
  if(m<=0):return None
  pv1,pv2=0,0
  pv1 = fv*(c/m)*(1-(1/(1+r/m)**(m*n)))/(r/m)
  pv2=fv/((1+r/m)**(m*n))
  return pv1+pv2

'''
solve()
paramaters: 
# Note: ONLY INPUT 3 Parameters to find the fourth one. Parameter 'm' will be set automatically. 
fv = Future Value
pv = Present Value 
r = Rate of Interest/Discount Rate (in decimals eg: 0.05 for 5%)
n = Number of Years
m = Frequency of Interest Calculation (eg: 2 for Semi-annually)

'''

#Calculation of missing variable among fv,pv,r,n
def solve(fv=-1,pv=-1,r=-1,n=-1,m=1):
  if(m<=0):return None
  if(fv==-1 and pv!=-1 and r!=-1 and n!=-1):
    fv = FV(pv,r,n,m)
    return fv
  if(pv==-1 and fv!=-1 and r!=-1 and n!=-1):
    pv = PV(fv,0,r,n,m)
    return pv
  if(r==-1 and fv!=-1 and pv!=-1 and n!=-1):
    r = m*(((fv/pv)**(1/m*n)-1))
    return r
  if(n==-1 and fv!=-1 and pv!=-1 and r!=-1):
    n = math.log(fv/pv)/(m*math.log(1+(r/m)))
    return n
  return None
