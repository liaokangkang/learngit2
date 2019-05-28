"""
打印三角形图案
"""
row=int(input('输入行数'))
for i in range (row):
	for j in range (i+1):
		print('*',end='')
	print()

for i in range (row):
	for j in range (row - i):
		print(" ",end='')
		continue
	for k in range (row-i,row+1):
		print("*",end='')
	print()

for i in range (row):
	for j in range (row -i-1 ):
		print(' ',end='')
	for k in range(2*i+1):#续接着第一行的序列
		print('*',end='')
	
	print()

