# coding:utf-8

# <第一種>

from datetime import datetime
# 得到当前日期时间（两种方法）
now = datetime.now()
# 得到当前日期
print(now.strftime('%d'))
print(datetime.today().replace(microsecond=0))
# 得到当前时间
print(datetime.strftime(now, '%H:%M:%S'))
# 得到当前年份用year_变量接收
year_ = now.strftime('%Y')
# 得到当前月份用month_变量接收
month_ = now.strftime('%m')
# 得到当前天用day_变量接收
day_ = now.strftime('%d')
# 使用-拼接年月日得到当前日期
print('{}-{}-{}'.format(year_, month_, day_))

# <第二種> -- 使用datetime中的now()和today()得到当前的时间

print('*' * 30)
print(datetime.today())
print(datetime.now())

print('=' * 30)

from datetime import datetime
# 定义一个str_字符串为2019-09-10 8:10:56
str_= '2019-09-10 8:10:56'
# 将str_转换为日期函数2019-09-10 8:10:56
str_date= datetime.strptime(str_, '%Y-%m-%d %H:%M:%S')
print(str_date)
# 定义now_变量接收当前的日期时间
now = datetime.now()
# 将当前日期时间格式化为——四位的年份/月/日 时:分:秒
date_str= now.strftime('%Y/%m/%d %H:%M:%S')
print(date_str)

# 小数点后边是微秒，可以使用datetime模块中的replace()方法，将参数microsecond微秒的值设置为0
