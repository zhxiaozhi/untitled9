# pass关键字在Python里没有意义，只是单纯的用来占位，保证语句的完整性

age = int(input('请输入您的年龄:'))

# if age > 18:
#     print('欢迎来到我的网站')
#     print('yes')
# print('hello')

if age > 18:
    pass # 使用Pass进行占位，没有意义，单纯为了保证语句完整性，使程序不报错
print('hello')