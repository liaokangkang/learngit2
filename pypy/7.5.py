def ifrun(years):
	return years%4==0 and years%100!=0 or years%400==0

def which_day(years,month,days):
	total=0
	if ifrun(years):
		a=[31,28,31,30,31,30,31,31,30,31,30,31]
	else:
		a=[31,29,31,30,31,30,31,31,30,31,30,31]
	for i in range(0,month-1):
		total+=a[i]
	return total+days

def main():
	print(which_day(1890, 2, 5))
	print(which_day(2000,8,20))
	print(which_day(2019,6,5))
	print(which_day(2018,1,1))

if __name__ == '__main__':#判断某年某月的某天是某年中的第几天
	main()