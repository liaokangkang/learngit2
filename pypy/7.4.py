def main(x):#一组数中取最大的两个
	m1=x[0]
	m2=x[1]
	if m1 < m2:
		m1=x[1]
		m2=x[0]
	for index in range(2,len(x)):
		if x[index]>m1:
			m1=x[index]
		elif x[index]>m2:
			m2=x[index]
	print(m1,m2) 
if __name__ == '__main__':
	main('4568971344543468')

