import os
import time
def main():
	s='北京欢迎您。。。。。'
	while True:
		os.system('cls')
		print(s)
		time.sleep(0.2)
		s=s[1:]+s[0]

if __name__ == '__main__':
	main()