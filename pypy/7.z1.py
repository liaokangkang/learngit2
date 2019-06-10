#双色球选号
from random import randint, sample 
def select():
	a=[x for x in range(1,34)]

	num=[]
	num=sample(a,6)
	num.sort()
	num.append(randint(1,16))
	return num

def sc(x):
	for index,ball in enumerate(x):
		if index == len(x)-1:
			print('|',end=' ')

		print('%02d'% ball,end=' ')
	print()


def main ():
	i = int(input('买几组'))
	for a in range(i):
		sc(select())


if __name__ == '__main__':
	main()