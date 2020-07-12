# Python中使用input 内置函数接收用户的输入
# input() ==> 括号里写提示信息
# 定义一个变量可以保存用户输入的内容
# password = input('请输入你的银行卡密码:')
# print(password)

# 注意：不管用户输入的是什么，变量保存的结果都是字符串
age = input('请告诉我你的年龄：')
print(age)
print(int(age)+1)
print(type(age))
