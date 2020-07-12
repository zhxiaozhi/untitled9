# 使用bool 内置类可以将其他数据类型转换成为布尔值

# 数字里，只有数字0 被转换成为布尔值是False，其他数字转换成为布尔值都是True
print(bool(100))   # 将数字100转换成为布尔值，True
print(bool(-1))    # 将数字-1转换成为布尔值，True
print(bool(0))     # 将数字0转换成为布尔值，False

# 字符串里，只有空字符串 '' / "" 可以转换成为Flase，其他字符串都转换成为True
print(bool('Hello'))    # True
print(bool('False'))    # True
print(bool(''))     # False
print(bool('\n'))   # True

#  空数据，None 转换成为布尔值是False
print(bool(None))   # False
print(bool('None'))    # True

print(bool([]))     # False,空列表
print(bool(()))     # False，空元组
print(bool({}))     # False，空字典

s = set()   # 空集合
print(bool(s))     # False，空集合


# 总结：数字0，空字符串''/ "",空列表[]，空元组()，空字典{}，空数据None，空集合()都会被转换成为False

# 在计算机里，True和False其实就是使用数字 1 和 0 保存的
print(True + 1)     # 2
print(False + 1)     # 1


# 隐式类型转换
if 3:
    print('good')
# 会打印good，3是True
if 0:
    print('good')
# 不会打印good，0是False
