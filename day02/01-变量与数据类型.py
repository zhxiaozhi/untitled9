# a 我们就称之为变量
a = '你好，世界'
print(a)

b = 35
print(b)


c = True
print(c)
print(type(c))

# 数据类型的概念
# 在Python里数据都有各自对应的类型

# 数字类型：整数型int 浮点型float 复数complex
print(45)  # int整数类型
print(3.1415)  # float浮点型
print((-1)**0.5)  # 复数complex

# 字符串类型：其实就是一段不同的文字
# python里面的字符串要求使用一对单引号，或者双引号来包裹
print('今天天气好晴朗，处处好风光呀好风光')
print('56')

# 布尔类型：用来表示真假/对错
# 布尔类型里一共只有两个值，一个是True，一个是False
print(4 > 3)  # 对，True
print(1 > 5)  # 错，False

# 列表类型
names = ['123', '321','qytang','cisco']
print(names)
# 字典类型
person = {'name':'张健','age':18,'addr':'China'}
print(person)
# 元组类型
nums = (1,5,6,7,8)
print(nums)
# 集合类型
x = {9, 'hello', 'hi', 'good', True}
print(x)
