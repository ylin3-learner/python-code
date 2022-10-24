# coding: utf-8

# finally -- 無論是否發生異常, 一定會執行的代碼塊 -- python 2.5以前, finally要單獨使用,不與try配合
# try語法至少要伴隨 except或finally其中一個
'''
try:
    <code1>
except:
    <code2>
finally:
    <code3>
'''

def test1():
    try:
        1 / 0
    except Exception as e:
        print(e)
    finally:
        return 'finally'

result = test1()
print(result)

def test2():
    try:
        1 / 0
    except Exception as e:
        print(111)
        return e  # 在這裡我們已經return了, 但finally依然打印出來了
    finally:
        print('finally')

print('-------')
result = test2()
print(result)

def test3():
    try:
        print('try test 11')
        return 'try'
    except Exception as e:
        print(e)
    finally:
        return 'finally'

print('- '* 30)
result = test3()
print(result)


# 雖然except, finally 都有return 且是自上而下進行, 但最終仍選擇finally執行
def test4():
    try:
        1 / 0
    except Exception as e:
        print(1)
        return e
    finally:
        print(2)
        return 'finally'

print('*' * 10)
result = test4()
print(result)


# try, except的返回誰優先級更高?

def test5():
    try:
        print('1try')
        return 'try' # return 有'try', 'finally'; 但最終還是強制執行了'finally'
    except Exception as e: # 因為try: 語句沒有出錯, 所以except語句沒有執行
        print('2finally')
        print('e')
    finally:
        return 'finally'

print('=======')
result = test5()
print(result)


def test6():
    try:
        print('try1')
        1 / 0  # 當遇到錯誤, 錯誤代碼後面的程序就沒有再執行 -- 直接進入了finally
        print('try3')
    finally:
        return 'i am finally'
print('--------')
print(test6())

def test_num():
    try:
        23 * 0 # 正確的邏輯 -- 不會報錯
    except Exception as e:
        print(e)
    finally: # 即使不報錯依然會執行
        print('finally')
print('**********')
test_num()

