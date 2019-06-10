#约瑟夫环问题
def main():
	person=[True]*30
	counter,number,index=0,0,0
	while counter<15:
		if person[index]:
			number+=1
			if number==9:
				person[index]=False
				counter+=1
				number=0
		index+=1
		index%=30
	for i in  person:
		print('基'if i else '非',end=' ')
	print()

if __name__ == '__main__':
	main()
