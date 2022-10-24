# coding:utf-8

# 時間戳/timestamp: since 1970/1/1 00:00:00's microsecond; type(timestamp)=float
'''
time.time() -- timestamp秒級別,
暫停函數: sleep(second) --second:希望程序被暫停的秒數
strftime, strptime
'''
'''
time.localtime(timestamp): timestamp可不傳,默認為最新時間
localtime對應字段介紹: 
tm_year, tm_mon, tm_day, tm_hour:0-23, tm_min:0-59
tm_sec:0-61, tm_wday:0-6, tm_yday:1-366, tm_isdst:-1,0,1是否是夏時令
'''
'''
time.strftime(format, t) -- t: time.localtime的時間類型
time.strptime(time_str:str, format) --format: 與time_str格式一致的格式化標準
'''
import time
import datetime

now = time.time() # 顯示地為觸發這句語句的時間
print(now, type(now))

time_obj = time.localtime(now)
print(time_obj, type(time_obj))
# time.sleep(5)
current_time_obj = time.localtime()
print(current_time_obj)

before = now - 100000 # 秒級別
before_time_obj = time.localtime(before)
print(before_time_obj)

print(time.time() * 1000) # 轉換為毫秒級別
print(time.time())

# for i in range(10):
#     print(i)
#     time.sleep(1)

'''
import datetime
now = datetime.datetime.now()
datetime.datetime.timestamp(now) -- 生成秒級的時間戳
now == datetime時間對象
datetime.datetime.fromtimestamp(timestamp) -- 返回datetime日期對象
# 包.模塊.函數
不同於time()生成時間戳, 將datetime對象轉成
'''
datetime_now = datetime.datetime.now()
datetime_timestamp = datetime.datetime.timestamp(datetime_now)
print('datetime 生成的时间戳 %s' % datetime_timestamp)

datetime_obj = datetime.datetime.fromtimestamp(datetime_timestamp) # package._py.func
print(datetime_obj)
