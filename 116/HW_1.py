from math116 import *


def fastGCD(a, b):
    x, y = a if a > b else b, b if a > b else a
    f, gcd, r = x, y, x % y
    while r > 0:
        f = gcd
        gcd = r
        r = f % gcd
    return gcd