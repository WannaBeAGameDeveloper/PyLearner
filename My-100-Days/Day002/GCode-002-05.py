"""
比较、逻辑和算身份运算符的使用

Version: 0.1
Author: 骆昊
"""

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1) # flag1 = True
print("flag2 = ", flag2) # flag2 = False
print("flag3 = ", flag3) # flag3 = False
print("flag4 = ", flag4) # flag4 = True
print("flag5 = ", flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False
