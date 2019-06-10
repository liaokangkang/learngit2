def main():
	str1='hello,world'
	print(len(str1))  #字符长度
	print(str1.upper())  #字符大写
	print(str1.capitalize())#字符首字母大写
	print(str1.find('or'))
	print(str1.find('d'))# 查找子串在字符串中的位置
	print(str1.startswith('h'))
	print(str1.startswith('o'))#判断字符是否以指定的子串作为开头
	print(str1.endswith('ld'))
	print(str1.endswith('fcuk'))#判断字符是否以指定的子串作为结尾
	print(str1.center(50,'*'))# 将字符串以指定的宽度居中并在两侧填充指定的字符
	print(str1.rjust(50,'%'))#将字符串以指定的宽度靠右放置左侧填充指定的字符
	str2='abc123456'
	print(str2[2])
	print(str2[1:])
	print(str2[1::4])#从位置1开始，每隔4个单位取出一个值，闭
	print(str2[-1])
	print(str2[-3:-1])#取-1 和-2位置上的字符
	print(str2[1:5])#取位置1到4的字符
	print(str2[::3])
	print(str2[::-1])#倒着来，每隔一个数取一个值
	print(str2[::-2])
	print(str2.isdigit())#判断字符是否是以数字组成
	print(str2.isalpha())#判断字符是否以字母组成
	print(str2.isalnum())#判断字符是否以字母和数字组成
	str3='    zbc'
	print(str3)
	print(str3.strip())#修剪字符串左右两边的空格

if __name__ == '__main__':
	main()