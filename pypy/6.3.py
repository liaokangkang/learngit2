#判断一个数是不是素数
def sh(n):
	go=True
	for i in range(2,n):
		if n%i==0:
			go=False	
	return go if n !=1 else False
print(sh(13)) 