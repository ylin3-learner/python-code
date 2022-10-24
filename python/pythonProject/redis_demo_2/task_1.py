# coding:utf-8

from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:  # with是Python裡面的context manager。可以管理檔案的使用與不使用，檔案用完自動關閉 -> 不需要f.close()
    file = open('考試成績.txt', 'r', encoding='utf-8')
    res = file.read().splitlines()  # splitlines()將數據切割
    print("data:", res, end='\n')
        # f.read()一口氣把所有的內容讀取，並且以字串的型態放入變數中。
    for one in res:
        print(one)
        temp = one.split(',')  # 因為原始數據使用","切割, 所以需要提取每個數據出來
        stu_no = temp[0]
        sname = temp[1]
        classno = temp[2]
        score_1 = int(temp[3])
        score_2 = int(temp[4])
        score_3 = int(temp[5])
        # 判斷條件: 任一score > 85
        if score_1 >= 85 and score_2 >= 85 and score_3 >= 85:
            # 將資料存入redis hashtable
            con.hmset(stu_no, {'name': sname, 'classno': classno,
                                'score_1': score_1, 'score_2': score_2, 'score_3': score_3})
    print('Successfully input')
except Exception as e:
    print(e)
finally:
    #　為何每次打開文件後，都須關閉文件? 關閉檔案可以釋放系統資源，避免資源的佔用導致其他程式無法順利運作。
    if 'flie' in dir():
        file.close()
        print('1')
    del con