#定义求最大公约数和最小公倍数的函数
def gcd(x,y):
	if x<y:
		(x,y)=(y,x)
	for i in range (x,0,-1):
		if x%i==0 and y%i==0:
			return i


def lcm(x, y):
    return x*y // gcd(x, y)


x=2
y=4
c=gcd(x,y)
d=lcm(x,y)
print('%d和%d的最大公约数是%d,最小公倍数是%d'%(x,y,c,d))

