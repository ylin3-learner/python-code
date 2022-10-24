# coding:utf-8

# 傳遞給map(),filter()和reduce()的函數通常只會使用一次，因此定義可引用函數通常沒有意義。
# 一次性的、匿名的函數，您只會使用一次且永遠不會再次使用 - 一個 lambda。
# map() -> all()
'''
def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(starts_with_A, fruit) # 直接調用可引用函數start_with_A, 不用加括弧

print(list(map_object))
>>>[True, False, False, True, False]
'''
'''
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit)

print(list(map_object))
>>>[True, False, False, True, False]
'''

fruits = ['apple', 'orange', 'banana']

res = filter(lambda x: 'e' in x, fruits)
print(list(res))  # 看似已被過濾掉, 但實際上只存在於filter對象中被忽略
print(fruits)

def filter_func(item):
    # if 'e' in item:
    #     return True # 判斷True, None
    return 'e' in item  # 只判斷True, False
'''
return True vs. return item
if(talksAbout(node.childNodes[i],string))
   return true;
檢查調用的返回，如果結果為真則返回真。

return taksAbout(node.childNodes[i],string)
返回迭代的第一項，而不檢查其餘項。
'''
print('--------')
filter_result = list(filter(filter_func, fruits))  # 對循環根據過濾條件進行過濾
print(filter_result)

# map(func是否滿足條件的判斷, list) -對列表中的每個成員依次執行函數, 將執行結果放到新list中, 返回map對象

map_result = map(filter_func, fruits)
print(list(map_result))  # None -> False
'''
reduce()map()與和的工作方式不同filter()。
它不會根據function我們傳遞的和迭代返回一個新列表。相反，它返回一個值。
'''
from functools import reduce

reduce_result = reduce(lambda x, y: x+y, fruits) # reduce(func對數據累加的函數, list) -對循環前後兩個數據進行累加或累乘
print(list(reduce_result))
print(reduce_result)
# 但字符串只可以累加, 不能累乘
reduce_result_1 = reduce(lambda x, y: x*y, [1, 2, 3, 4])
print(reduce_result_1)

ls = [1, 2, 3, 4]
map_test_result = list(map(str, ls))
print(map_test_result)

