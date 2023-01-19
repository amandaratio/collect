
def fast2Power(a, n, m):#jsjs
    x = 1
    while n > 0:
        a = (a^2) % m
        if n % 2 == 1:
            x = (x * a) % m
        n = n // 2 
    return x


