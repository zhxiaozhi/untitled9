a = '12.34'
# 使用内置float类 可以将其他类型数据转换成为float浮点数
b = float(a)
print(b + 1)

# 如果字符串不能被转换成为有效的浮点数，会报错
# c = float('hello')
# print(c)


c = 101
print(float(c))     # 101.0

m = float('12')     # 将字符串转换成为浮点数
n = float(12)   # 将整型转换成为浮点数
print(m, n)