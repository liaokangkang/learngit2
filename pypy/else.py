#求分段函数的值
x=float(input('x='))
f=0
if x>1:
	f=3*x-5
elif x>=-1:
	f=x+2
else:
    f=5*x+3 
print('f(%.2f) = %.2f' % (x,f))
#print('f(%.2f) = %.2f' % (x, y))