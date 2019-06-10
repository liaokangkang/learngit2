  # 列表切片
   # fruit3 = fruits  # 没有复制列表只创建了新的引用
    # 可以通过完整切片操作来复制列表
      # 可以通过反向切片操作来获得倒转后的列表的拷贝
def main():
 	list1=['apple','grapes','banana','orange']s
 	list1 +=['strawberry','pear']
 	for fruit in list1:
 		print(fruit.title(),end=' ')#循环遍历列表元素
 	print()
 	print(list1)
 	print(list1[1:3])
 	print(list1[::-1])
 	print(list1[1::])
 	list2=sorted(list1)#默认按字母顺序排列
 	print(list2)
 	list3=sorted(list1,reverse=True)
 	list4=sorted(list1,key=len)
 	print(list1)
 	print(list2)
 	print(list3)
 	print(list4)
 	list1.sort(reverse=True)
 	print(list1)

if __name__ == '__main__':
	main()