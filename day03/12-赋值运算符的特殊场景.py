# 等号连接的变量可以传递赋值
a = b = c = d = 'hello'
print(a, b, c, d)

# x = 'yes' = y = z     错误，赋值运算时从右到左。y不能赋值‘yes’


m, n = 3, 5  # 拆包，（3，5）是一个元组
print(m, n)

x = 'hello', 'good', 'yes'
print(x)   # ('hello', 'good', 'yes')

# 拆包时，变量的个数和值的个数不一致，会报错
# y,z = 1, 2, 3, 4, 5
# print(y,z)
# o, p, q = 4, 2
# print(o, p, q)

# *表示可变长度，p是可以变的
# o, *p, q = 1, 2, 3, 4, 5, 6
# print(o, p, q)  # 1 [2, 3, 4, 5] 6


# o是可以变的
# *o, p, q = 1, 2, 3, 4, 5, 6
# print(o, p, q)  # [1, 2, 3, 4] 5 6

o, p, *q = 1, 2, 3, 4, 5, 6
print(o, p, q)  # 1 2 [3, 4, 5, 6]

