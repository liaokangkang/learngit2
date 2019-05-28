"""
输入两个正整数计算最大公约数和最小公倍数
"""
a=int(input('输入第一个数'))
b=int(input('输入第二个数'))
if a>b:
    a,b=b,a
for facter in range(a,0,-1):
    if a%facter==0 and b%facter==0:
    	print("%d和%d的最大公约数是%d" % (a,b,facter))
    	print("%d和%d的最小公倍数是%d " % (a,b,a*b//facter))
    else:
    	break

    	
