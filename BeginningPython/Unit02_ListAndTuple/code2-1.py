#代码清单2-1 索引实例
#根据给定的年月日以数字形式打印出日期

months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
]

#以1~31的数字作为结尾的列表
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] \
		+ ['st']

year = input('Year:')
month = input('Month(1~12):')
day = input('Day(1~31):')

month_val = eval(month)
day_val = eval(day)

#因为索引从0开始，所以索引的计算公式为index = val - 1 
month_name = months[month_val - 1]
ordinal = day + endings[day_val - 1]

print("{} {}, {}".format(month_name, ordinal, year))
input()
