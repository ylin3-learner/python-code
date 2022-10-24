# coding:utf-8

# datetime package = date + time -- current time, 時間間隔, 時間對象<->時間字符串
# 如果用import datetime >> 使用: datetime.datetime.func() -- package. _.py.func()
# date.strftime(format) -- ('%Y-%m-%d %H:%M:%S')
# date.strptime(tt,format) -- tt為符合時間格式的字浮串, format: tt時間字符串匹配規則(時間與時間之間的相連格式要統一)

from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now, type(now)) # type(now) -- <class 'datetime.datetime'>
now_str = now.strftime('%Y-%m-%d %H:%M:%S') # 轉成時間字符串
print(now_str, type(now_str))

now_obj = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S') # 轉成時間格式
print(now_obj, type(now_obj), '----')

three_days = timedelta(days=3) # timedelta為時間間隔對象 --days, hours, minutes,...要加s
after_three_day = now + three_days
print(after_three_day)
after_three_day_str = after_three_day.strftime('%Y/%m/%d %H:%M:%S')  # 轉成時間字符串
print(after_three_day_str, type(after_three_day_str))
after_three_day_obj = datetime.strptime(after_three_day_str, '%Y/%m/%d %H:%M:%S')
# 轉成時間格式 -- 必須要和時間字符串格式保持一致
print(after_three_day_obj, type(after_three_day_obj), '----')

before_three_day = now - three_days
print(before_three_day)
before_three_day_str = before_three_day.strftime('%Y%m%d')  # 轉成時間字符串
print(before_three_day_str, type(before_three_day_str))
before_three_day_obj = datetime.strptime(before_three_day_str, '%Y%m%d')  # 轉成時間格式
print(before_three_day_obj, type(before_three_day_obj), '-----')

one_hour = timedelta(hours=1)
before_one_hour = now - one_hour
print(before_one_hour)
before_one_hour_str = before_one_hour.strftime('%H:%M:%S')  # 轉成時間字符串
print(before_one_hour_str, type(before_one_hour_str))

# default_str = '2020 12 abc'
# print(datetime.strptime(default_str, '%Y %m')) -- unconverted data 'abc'
'''
%I - 一天中的第幾個小時(0-12), %M: 當前的第幾分(0-59), %S: 當前分的第幾秒(0-61),因為閏年多佔2秒,  %f: 當前秒的第多少毫秒
%a: 簡化的星期: Wed,  %A: 完整的星期Wednesday,  %b: 簡化的月份Feb,  %B: 完整的月份February
%c: 本地的日期和時間,  %p: 顯示上午還是下午(AM/PM),  %j: 一年中的第幾天,  %U: 一年中的星期數
'''


