#判断输入的年份是不是闰年

y = eval(input('请输入年份:'))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
	print('{}年是闰年！'.format(y))
else:
	print('{}年不是闰年！'.format(y))