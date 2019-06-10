def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
print(is_palindrome(65))
#求出反过来的数值，输入54 求出45 不相等，输出False