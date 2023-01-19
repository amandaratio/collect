from math116 import *
import math

def factorPolland(N, a=2, m=1000000):
    # N is the number to factor, a is a number 1 < a < N, and m is the limit for the factorial
    for j in range(2, m):
        a = fast2Power(a, j, N)
        d = fastGCD(a-1, N)
        if d == N:
            return "a = {} failed. Try new a.".format(a) 
        if 1 < d and d < N:
            # nontrivial factor => success
            return d 
    return "Not Found"
print(factorPolland(7648424392789))