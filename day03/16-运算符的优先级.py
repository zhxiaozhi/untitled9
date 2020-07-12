print(10 - 2 * 3)   # 4
print(10 + 2 * 3 ** 2)  # 28,先进行幂运算

# 逻辑运算的优先级：not > and > or
# 和短路无关
print(True or False and True)   # True
print(False or not False)   # True
print(True or True and False)   # True

# 强烈建议：在开发中，使用括号来说明运算符的优先级
print(True or True and False)
print(True or (True and False))     # 手动加括号进行辨识优先级

# 逻辑运算符的规则
# 逻辑与运算：
# 只要有一个运算数是False，结果就是False；只有所有都是True，结果过才是True
# 只要遇到False，就停止，不在执行！
# 取值：取第一个为False，如果所有的运算数都是True，取最后一个运算数

# 逻辑或运算：
# 只要有一个运算数是True，结果就是True；只有所有都是False，结果过才是False
# 只要遇到True，就停止，不在执行！
# 取值：取第一个为True，如果所有的运算数都是False，取最后一个运算数
