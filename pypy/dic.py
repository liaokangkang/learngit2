def main():
	scores={'赵':99,'钱':80,'孙':78,'李':80}  #字典，用空间换时间
	#通过健获取字典对应的值，即根据字母查字典
	print(scores['赵'])
	print(scores['李'])
	for elem in scores:
		print('%s的分数是%d'%(elem,scores[elem]),end=' ')#遍历所有元素
	print()

	scores['张']=59
	scores['黄']=58
	scores.update(乌龟=40,鸡毛=54)#添加元素
	print(scores)
	if '吴' in scores:
		print(scores['吴'])
	print(scores.get('吴'))
	print(scores.get('吴',10))
	#删除字典中的元素
	print(scores.popitem())
	print(scores.popitem())
	print(scores.pop('孙'))
	#清空字典
	scores.clear()
	print(scores)








if __name__ == '__main__':
	main()