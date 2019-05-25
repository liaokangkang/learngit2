"""
判断输入的三边能不能构成三角形
并输出面积
"""
import math
a= float(input('输入一个数'))
b=float(input('输入一个数'))
c=float(input('输入一个数'))
if a+b>c and a+c>b and b+c>a:
	C=a+c+b
	S=math.sqrt(C*(C-a)*(C-b)*(C-c))
	print('面积是%f'%(S))
else:
	print("三边无法构成三角形")