# coding:utf-8

import threading


class Candy(object):
    def __init__(self):
        self.childs = list(range(1, 6))
        self.candys = list('candy' for _ in range(100))  # 相當於有100個 'candy'
        # 其中’_’ 是一个循环标志，也可以用i，j 等其他字母代替，類似於普通變量，只是不取值，只循環，這個” _"就是一個佔位符。
        self.res = {}
        self.count = 0

    def divide_candy(self):
        candy = []
        while len(self.candys) > 0:
            if len(candy) < 20:
                c = self.candys.pop()
                candy.append(c)
                if len(candy) == 20:
                    self.res[self.childs[self.count]] = candy
                    self.count += 1
                    '''
                    上方兩行能使得 'candy' 所有的 'candy' 都能夠呈現
                    '''

    def thread(self):
        for _ in self.childs:
            t = threading.Thread(target=self.divide_candy)
            t.start()


if __name__ == '__main__':
    one_child = Candy()
    one_child.thread()
    print(one_child.res)



