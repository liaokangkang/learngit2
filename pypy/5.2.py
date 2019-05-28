#寻找0到1000内的完美数，它所有的真因子（即除了自身以外的约束）的和等于本身

for i in range(1,1000):
	sum=0
	for k in range (1,i):
		if i%k==0:
			sum=sum+k
	if sum==i:
		print('%d是完美数' % i)
	

