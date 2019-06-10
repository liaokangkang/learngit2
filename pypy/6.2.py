#判断一个数是不是回文数
def hws(n):
	a=n
	t=0
	while a>0:
		t=t*10+a%10
		a=a//10
	return t==n
print(hws(12321))
print(hws(123456))