from fractions import Fraction
import math
n, k = map(int,input().split())
n_fac = math.factorial(n)
k_fac = math.factorial(k)
nk_fac = math.factorial(n-k)
print(Fraction(n_fac, (k_fac*nk_fac))%10007)