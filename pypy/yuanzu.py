def main():
	t=('叮当',88,True,'南京')
	print(t)
	print(t[0])
	print(t[3])
	#t[0]='sd'  报错
	for member in t :
		print(member)
	t =('大熊',6,True,'北极')#重新给元组赋值
	print(t)
	person =list(t)   #将元组转化为列表，list是可以修改的
	print(person)
	person[0]='多多'
	print(person)
	f=['apple','grapes','orange']#list是【】，元组是（），元组是不可修改的
	ft=tuple(f)
	print(ft)


if __name__ == '__main__':
	main()