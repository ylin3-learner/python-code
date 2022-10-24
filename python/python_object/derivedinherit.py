# coding:utf-8

# class child(Parent1, Parent2, Parent3...)

# 1. 2個父類

class Tool(object):
    def work(self):
        return 'tool work'

    def car(self):
        return 'car will run'

class Food(object):
    def work(self):
        return 'food work'

    def cake(self):
        return 'i like cake'

# 繼承父類的子類
class Person(Tool, Food): # 由左至右繼承
    pass

if __name__ == '__main__':
    p = Person()
    p_car = p.car()
    p_cake = p.cake()
    print(p_car,'\n',p_cake)

    p_work = p.work()
    print(p_work)  # >>tool work, 因為先繼承Tool,再Food

    print(Person.__mro__) # 會返回 類是如何繼承的和繼承順序
    # >> (<class '__main__.Person'>, <class '__main__.Tool'>, <class '__main__.Food'>, <class 'object'>)