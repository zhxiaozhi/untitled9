# 1.区间判断
score = float(input('请输入您的成绩：'))
# 在某些语言里，判断区域不能连写
# 在有些语言里，需要使用逻辑运算符来连接 score >= 0 and score < 60
# python里可以使用连续的区间判断
if 60 > score >= 0:
    print('你个垃圾')

# 2.隐式类型转换
if 4:    # if后面需要的一个bool类型的值。# 如果if后面不是不尔类型，会自动转换成为布尔类型
    print('hello world')

# 3.三元表达式(对if...else语句的简写)

num1 = int(input('请输入一个数字:'))
num2 = int(input('请输入一个数字:'))

# if num1 > num2:
#     x = num1
# else:
#     x = num2

x = num1 if num1 > num2 else num2
# x等于num1，如果num1大于num2，取num1.如果不满足num1>num2，x等于num2

print('两个数里的较大数是', x)





