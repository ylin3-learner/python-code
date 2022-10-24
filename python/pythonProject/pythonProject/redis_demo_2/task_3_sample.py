# coding:utf-8

from concurrent.futures import ThreadPoolExecutor, as_completed

def say_hello_to(names):
    print('say hello to {}'.format(names))

names = ['Tony', 'Ian', 'Penny', 'Angel']

with ThreadPoolExecutor(max_workers=5) as executor:
    for n in names:
        executor.submit(say_hello_to, n)

print('------------------------')
# 前述範例多執行幾次，有可能會遇到文字列印時黏在一起的情況，這是由於多個 Thread 同時都想輸出文字而造成的情況
# say hello to Pennysay hello to Angel

# 事實上，當呼叫 submit 後，會回傳的並不是在 Thread 執行的程式結果，而是 Future 的實例，而這個實例是一個執行結果的代理(Proxy)
# 透過 done , running , cancelled 等方法詢問 Future 實例在 Thread 中執行的程式狀態
# 如果程式已經進入 done 的狀態，則可以呼叫 result 取得結果

def say_hello(name):
    return f'Hi from {name}'

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for name in names:
        future = executor.submit(say_hello, name)
        print(type(future))
        futures.append(future)  # 取得 future 實例之後，放進 futures list 中

    for future in futures:  #　透過 as_completed(futures) 一個一個取得已經完成執行的 future 實例
        print(future.result())  # 透過 result() 取得其結果後並列印出來
print('------------------')
'''
由於我們將列印的功能從 Thread 內搬出，所以也解決列印文字可能黏在一起的情況。
'''


# 也可以直接利用 map() 方法直接取得 Thread 的執行結果

def say_hello_to(name):
    for i in range(100000):
        pass
    return f'Hi, {name}'


names = ['John', 'Ben', 'Bill', 'Alex', 'Jenny']

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(say_hello_to, names)

for r in results:
    print(r)