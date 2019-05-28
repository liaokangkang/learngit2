#寻找100到1000内的水仙花数 
for i in range(100,1000):
	a = i //100
	b = (i-a*100)//10
	c = i-a*100-b*10
	if pow(a,3)+pow(b,3)+pow(c,3)==i:
		print('%d是水仙花数'% i )

