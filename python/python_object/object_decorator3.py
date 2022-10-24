# coding:utf-8

# staticmethod -- 類函數可不經實例化而調用, 被調用函數不許傳self,cls; 且無法在該函數內調用其他類函數或類變量

'''
@staticmethod
def func():
    do
'''
class test(object):
    @staticmethod
    def add(a, b):
        return a + b

print(test.add(1, 2))
