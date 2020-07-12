# 逻辑与and运算，只有所有运算数都是True，结果才是True
# 只要有一个运算数是False，结果就是False
4 > 3 and print('hello world')  # 4>3是True，and需要两个都是True，继续往下走，打印‘hello world’
4 < 3 and print('你好世界')     # 逻辑与运算的短路问题，4<3已经是Flase，不会再往下走

# 逻辑或or运算，只有所有的运算数都是False，结果才是False
# 只要有一个True，结果就是True
4 > 3 or print('哈哈哈')   # 4>3是True，or只要有一个True就是True，后面不会打印
4 < 3 or print('嘿嘿嘿')   # 4<3是False，or继续往下走，打印‘嘿嘿嘿’

# 逻辑运算的结果，一定是布尔值吗？
# 逻辑与and运算做取值时，取第一个为False的值；如果所有的运算数都是True，取最后一个值
print(99 or 100)    # 99
print(99 and 100)   # 100

print(3 and 5 and 0 and 'hello')    # 0，逻辑与and遇到0是False直接停了，所以就是0

print('good' and 'yes' and 'ok' and 100)   # 100

# 逻辑或运算做取值时，取第一个为True的值;如果所有的运算数都是False，取最后一个值
print(0 or [] or 'lisi' or 5 or 'ok')   # lisi
print(0 or [] or '' or ())  # ()

