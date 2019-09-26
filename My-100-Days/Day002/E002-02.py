#输入圆的半径计算周长和面积


import math

r = eval(input('请输入圆的半径:'))
l = math.pi * 2 * r
s = math.pi * (r ** 2)

print('半径为{}的圆，周长为{}，面积为{}'.format(r, l, s))

input() 