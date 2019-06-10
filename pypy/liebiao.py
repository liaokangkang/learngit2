def main():
	list1 = [1,3,5,7,100]
	print(list1)
	list2 = ['hello']*5
	print(list2)
	print(list1[2])
	print(list1[-2])
	list1[3]=1000
	print(list1)
	list1.append(200)# 添加元素
	list1.insert(1,4)#在1号位置插入4
	list1 +=[333, 344]#添加多个元素
	print(list1)
	print(len(list1))
	list1.remove(3)#删除元素
	if 1233344  in list1:
		list1.remove(1234)
	del list1[0]  #删除变量list1[0]，解除list1对其的引用
	print(list1)
	list1.clear()
	print(list1)










if __name__ == '__main__':
	main()