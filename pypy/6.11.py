def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)



x=2
y=4
c=gcd(x,y)
d=lcm(x,y)
print('%d和%d的最大公约数是%d,最小公倍数是%d'%(x,y,c,d))