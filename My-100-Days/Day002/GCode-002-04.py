"""
赋值和算术运算符的使用

Version: 0.1
Author: 骆昊
"""

a = 10
b = 3
print('a + b = {}'.format(a + b)) # 13
print('a - b = {}'.format(a - b)) # 7
print('a * b = {}'.format(a * b)) # 30
print('a / b = {}'.format(a / b)) # 3.3333333333333335
print('a // b = {}'.format(a // b)) # 3
print('a ** b = {}'.format(a ** b)) # 1000
print('(a - 1) ** 0.5 = {}'.format((a - 1) ** 0.5)) # 3.0
c = 4
c += b # 相当于：c = c + b
c *= a + 2 # 相当于：c = c * (a + 2)
print('c = {}'.format(c)) # 想想这个地方是多少
