def main():
	set1={1,2,3,3,3,2}  
	print(set1)#输出集合会自动剔除重复项
	print('Length=' ,len(set1))
	set2=set(range(1,10))
	print(set2)
	set1.add(4)
	set1.add(5)
	set2.update([11,12])#添加两个元素
	print(set1)
	print(set2)
	set2.discard(11)#删除某个元素，如果不存在，则报错
	print(set2)
	for ele in set2:
		print(ele,end=' ')
	print()
	set3=set((1,2,3,3,2,1))#将元组转化为集合
	print(set3.pop())#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
	print(set3)
	print(set1 & set3) #取交集
	print(set1|set2)#取并集
	print(set1 - set2)#取差集
	print(set1^set2)#对称差运算
	print(set2 <= set1)
	print(set3 <= set1)#判断子集和超集
	print(set1 >=set2)
if __name__ == '__main__':
	main()