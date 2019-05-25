"""
计算机随机抽取0——100之间的一个数由人来猜
计算即根据人猜的数据分别给出提示，带一点还是小一点
"""
import random
b= random.randint(1,100)
counter = 0
while  True:
	counter=counter+1
	a=int(input("输入一个0-100之间的数"))
	if a==b:
		print('猜中了')
		break
	elif a >b:
		print('大了点')
	elif a<b:
		print('小了点')
print('你一共猜了%d次' % counter)
if counter>7:
	print("你的智商余额显示不足")