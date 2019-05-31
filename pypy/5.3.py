#百钱百鸡问题
for i in range(0,101):
	for j in range(0,101):
		if 3*i+5*j+(100-i-j)/3==100:
			print("母鸡数量是%d,公鸡数量是%d,小鸡数量是%d" % (i,j,100-i-j))
