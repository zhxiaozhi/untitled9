# 使用int 内置类可以将数据转换成为整数

a = '31'
b = int(a)
print(a)
print(type(a))  # <class 'str'>
print(b)
print(type(b))  # <class 'int'>

# 如果字符串不是一个合法的数字，会直接报错
# x = 'hello'
# y = int(x)
# print(y)


x = '1a2c'
y = int(x, 16)  # 把字符串1a2c 当作十六进制转换成为整数
print(y)    # 6700 打印一个数字，默认使用十进制输出

m = 'a1f'
n = int(m, 16)
print(bin(n))

c = '123'
d = int(c, 8)   # 把字符串‘12’ 当做八进制转换成为整数
print(d)
