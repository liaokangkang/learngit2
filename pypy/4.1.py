#判断一个树是不是素数
from math import  sqrt
a=int(input('输入一个大于1的数'))
b=int(sqrt(a))
k=True
for i in range (2,b+1):
	if  a%i == 0:
		k=False
		break
if k:
    print('%d是素数' % a)
else:
	print('%d不是素数' % a)



