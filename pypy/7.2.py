import random
def main(n=4):
	s='0123456789qwertyuioplkmjnhbgvfcdxsza'
	lenth=len(s)
	code=' '
	for i in range(n):
		index=random.randint(1,lenth-1)
		code+=s[index]

	print(code)

if __name__ == '__main__':
	main()