# coding:utf-8

class Person(object):
    # 重写实例对象的构造（初始化）方法
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    # 自定义实例方法，格式化打印实例属性name的值
    def speak(self):
        print(f'hello 我是{self.name}')
    # 自定义实例方法，占位作用
    def relation(self):
        print('*' * 18)
class Student(Person):
     # 重写实例对象的构造（初始化）方法，并调用父类构造方法，实现对实例属性的赋值
    def __init__(self, name, gender, score=None, major=None, stu_num= '2018014002'):
        # 在定义Student类的构造函数时，设置了3个参数，但创建实例对象时传入了4个，因此会报错
        super(Student, self).__init__(name, gender)
        self.gender = gender
        self.score = score
        self.major = major
        self.__stu_num = stu_num
    def speak(self):
        super(Student, self).speak()
        print(f'我的学号是{self.__stu_num},很高兴认识大家')
     # 自定义实例方法，格式化打印实例属性stu_num的值
    def identify_stu(self):
       if  self.__stu_num=='2018014002':
           print('我的分组已经完成')
     # 自定义实例方法，判断学号是否为既定值，并根据判断结构 进行分类打印
       else:
            print('请稍后，马上为你自动分组')
     # 自定义实例方法，设置实例对象的学号为传入的值
    def set_num(self, new_num):  # set_num()是Student类中的实例方法，要放在Student类中
        self.__stu_num = new_num # 此处双下划线__定义的属性是私有属性，只能在类中使用，不能在类的外部调用。
     # 自定义实例方法，判断该类是否为Person类的子类，并进行分类打印
    def relation(self):
        if isinstance(Student(object, Student), Person) == True:
            print('我的父类是Person')
        else:
            print('父类正在查询中······')
if __name__ == '__main__':
    stu = Student('小明', '男', 90, '数学')
    # 调用speak方法 打印stu对应的值
    stu.speak()
    # 调用实例方法 鉴别学号是否为指定值
    stu.identify_stu()
    # 调用实例方法 鉴别实例对象所属的类的父类是否为Person
    stu.relation()
    print("******************")
    stu_2 = Student('小红', '女', 89, '英语')
    # 调用实例方法 设置stu_2的学号为'2018040625'
    stu_2.set_num('2018040625')
    # 调用实例方法 打印stu_2对应的值
    stu_2.speak()
    # 调用实例方法 鉴别学号是否为指定值
    stu_2.identify_stu()