#判断，闰年是True,否则是flase
year=int(input('请输入年份'))
a=(year % 4 ==0 and year % 100!=0 or year % 400 ==0)
print(a)