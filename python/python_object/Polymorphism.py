# coding:utf-8

'''
允許你將父對象設定成為和一個或更多的他的子對象相等的技術，
賦值之後，父對象就可以根據當前賦值給它的子對象的特性以不同的方式運作
'''
# 1.書寫一個父類
class XiaomuFather(object):
    def talk(self):
        print('小木的爸爸說了一句話')
    def jump(self):
        print('Everyone can jump')
# 2.書寫一個子類, 並且繼承一個父類-- 多態: 子類中重寫父類的函數
class XiaomuBrother(XiaomuFather):
    def run(self):
        print('小木的哥哥在奔跑著...')

    def talk(self):
        print('小木的哥哥在說話')

# 為甚麼要多態?
# 為甚麼要去繼承父類?
# 答案: 為了使用已經寫好的類中的函數, 為了保留子類中某個和父類名稱一樣的功能
# 可以幫助我們保留子類中的函數功能

class Xiaomu(XiaomuFather):
    def talk(self):
        print('哈哈! 小木也可以說自己的觀點')
if __name__ == '__main__':
    xiaomu_brother = XiaomuBrother()
    xiaomu_brother.run()
    xiaomu_brother.talk()

    father = XiaomuFather()
    father.talk()

    xiaomu = Xiaomu()
    xiaomu.talk()
# 沒有使用多態
    xiaomu.jump()
    xiaomu_brother.jump()