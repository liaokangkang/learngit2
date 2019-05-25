#掷骰子决定做什么事
from random import randint
a=randint(1,6)
if a==1:
	print("吃饭")
elif a==2:
	print("睡觉")
elif a==3:
	print("跑步")
elif a==4:
	print("爬山")
elif a==5:
	print("踢足球")
else:
	print("唱歌")