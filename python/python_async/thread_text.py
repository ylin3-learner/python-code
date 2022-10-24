# coding:utf-8

# random.choice(seq) - 從非空序列 seq 回傳一個隨機元素。如果 seq 為空，則引發 IndexError。
# 先定義一個列表, 在隨機獲取並從舊列表中刪除, 添加到新列表
# 使用多線程減少運行時間
import random
import time
import threading

lists = [
    'python', 'django', 'flask', 'tornado',
    'bs5', 'requests', 'uvloop'
]

new_list = []

def work():
    if len(lists) == 0: # 代表資料已被刪光
        return  # 不再進行下方業務
    data = random.choice(lists)
    lists.remove(data)
    new_data = '%s_new' % data
    new_list.append(new_data)
    time.sleep(1)  # 用以判斷work函數執行的速度

if __name__ == '__main__':
    start = time.time()
    print('old list len:', len(lists))
    t_list = []
    for i in range(len(lists)):
        t = threading.Thread(target=work)
        t_list.append(t)  # 傳入每個線程對象
        t.start()
        # 希望線程可以阻塞, 等到work全部執行完成, 在打印下方語句
    for t in t_list:
        t.join()

    print('old list: %s' % lists)
    print('new list: %s ' % new_list)
    print('new list len:', len(new_list))
    print('time is %s' % (time.time()-start))  # 標黃表示編譯器認為是time.time()在跟str格式化
