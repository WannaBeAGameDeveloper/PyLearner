#华氏温度转换为摄氏温度
#转换公式： F = 1.8 * C + 32

F = eval(input('请输入华氏温度: '))
C = (F - 32) / 1.8
print('{}℉ = {}℃'.format(F, C))
input()