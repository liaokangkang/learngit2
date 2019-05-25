"""
#百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E
"""
s=float(input('请输入分数'))
if s>89:
	grade='A'
elif s>79:
	grade ='B'
elif s>69:
	grade="C"
elif s>59:
	grade ="D"
else :
	grade = 'E'
print("成绩等级是: ",  grade)
