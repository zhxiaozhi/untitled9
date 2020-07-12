score = float(input('请输入您的成绩：'))

# if score >= 60:
#     print('及格了')
# else:
#     print('不及格')


# 0-60不及格，60-80及格，80-90良好，90-100优秀
# 多个if语句，语句和语句之间，不存在关联。每一个语句都会走
# if 60 > score >= 0:
#     print('你个垃圾')
# if 80 > score >= 60:
#     print('一般般')
# if 90 > score >= 80:
#     print('还不错')
# if 100 >= score >= 90:
#     print('好棒棒哟')

# 需要使用if...elif语句实现多重判断，更加优化
# 匹配到某个判断，就直接结束，不需要继续往下走
if 60 > score >= 0:
    print('你个垃圾')
elif 80 > score >= 60:
    print('一般般')
elif 90 > score >= 80:
    print('还不错')
elif 100 >= score >= 90:
    print('好棒棒哟')
else:
    print('好好输入你的成绩！')

