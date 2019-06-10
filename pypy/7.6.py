def main():
	num=int(input('输入杨辉三角的边长='))
	b=[[]]*num
	for i in range(len(b)):
		b[i]=[None]*(i+1)
		for j in range(len(b[i])):
			if j == 0 or j == i:
				b[i][j]=1
			else:
				b[i][j]=b[i-1][j]+b[i-1][j-1]
			print(b[i][j],end='\t')
		print('\t')


if __name__ == '__main__':
	main()
