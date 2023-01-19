
# ************* HW_2.py ************* #
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



# ************* HW_1.py ************* #


def fastGCD(a, b):
    x, y = a if a > b else b, b if a > b else a
    f, gcd, r = x, y, x % y
    while r > 0:
        f = gcd
        gcd = r
        r = f % gcd
    return gcd


# ************* HW_0.py ************* #


def fast2Power(a, n, m):#jsjs
    x = 1
    while n > 0:
        a = (a^2) % m
        if n % 2 == 1:
            x = (x * a) % m
        n = n // 2 
    return x



