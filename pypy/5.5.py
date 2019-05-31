"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""
import random as r
money=1000
counter=0
while money>0:
	print('你的总资产为%d'%money)
	need_go_on=False
	while True:
		debt=int(input('请下注'))
		if debt>0 and debt <=money  :
			break
	result=r.randint(1,6)+r.randint(1,6)
	print('玩家摇出的骰子数是%d'% result)
	print('')
	if result==7 or result==11:
		money+=debt
		print('你获胜了')
	elif result==2 or result ==3  or result==12:
		money-=debt
		print('庄家获胜')
	else:
		need_go_on=True


	while need_go_on:
	    result1=r.randint(1,6)+r.randint(1,6)
	    print('玩家再次摇出的骰子数是%d'% result1)
	    if result1==7:
		    money-=debt
		    print('庄家获胜')
		    need_go_on=False
	    elif result1==result:
		    money+=debt
		    print('你获胜了')
		    need_go_on=False

print('你的钱输光了')



