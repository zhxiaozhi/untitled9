# 进制转换是将int类型以不同的进制表示出来
# 类型转换将一个类型的数据转换为其他类型的数据
# int==>str str==>int bool==>int

age = input('请输入您的年龄：')
# 原因：intput 接收到的用户输入，都是str字符串类型
# 在Python里，如果字符串和数字做加法运算，会直接报错
# 把字符串类型的变量 age 转换成为数字类型的age
# print(age+1)  错误

# 使用int 内置类可以将其他类型的数据转换成为整数
print(type(age))    # <class 'str'>
print(int(age)+1)
print(type(int(age)))   # <class 'int'>

# 为什么要转换数据类型：因为不同的数据类型，进行运算时，他的运算规则是不一样的
