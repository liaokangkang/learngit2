def main(filename,t=False):
	a=filename.rfind('.')
	l=len(filename)-1
	if 0<l-a<l:
		index=a if t else a+1
		d= filename[a:]
		print(d)


if __name__ == '__main__':
	main('sss.rrr')#获取文件后缀名


