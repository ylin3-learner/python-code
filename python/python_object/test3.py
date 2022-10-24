# coding:utf-8

# 可以{{}}代表大括号
class  Point(object):
    # 自定义Point类的构造(初始化)方法
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 自定义Point类对象的格式化输出函数(string())
    def string(self):
        print('{x: %s, y: %s}' % (self.x, self.y))
class  Circle(Point):
    # 自定义Circle类的构造(初始化)方法
    def __init__(self, radius, x, y):
        super(Circle, self).__init__(x, y)
        self.__radius = radius
    # 自定义Circle类对象的格式化输出函数(string())
    def string(self):  # 可以{{}}代表大括号
        print('该图形初始化点为：{{ X：{}, Y：{} }}; {{ 半径为：{} }}'.format(
            self.x, self.y, self.__radius
        ))
class Size(object):
    # 自定义Size类的构造(初始化)方法
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 自定义Size类对象的格式化输出函数(string())
    def string(self):
        print('{Width：{}, Height: {}}'.format(
            self.width, self.height
        ))
class Rectangle(Point, Size):

    # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)
        '''
        在多重继承情况下，继承的父类中都有__init__()初始化函数，
        使用super( )函数只能继承第一个父类初始化函数，并未继承Size类的初始化函数，
        所以需要对self.width和self.height赋值，可以在子类中使用Size.__init__( )继承Size中的初始化函数，
        就不需要再给width和height赋值了
        '''

    # 自定义Rectangle类对象的格式化输出函数(string())
    def string(self):  # 可以{{}}代表大括号
        print(f'该图形初始化点为：{{ X：{self.x}, Y：{self.y} }}; 长宽分别为：{{ Width：{self.width}, Height：{self.height} }}')
if __name__ == "__main__":
    # 实例化Circle对象，圆心为（5,5），半径为8
    c = Circle(radius=8, x=5, y=5)
    c.radius = 15 # 因為設置為私有變量, 無法外部修改
    c.string()
    # 实例化Rectangle对象，顶点位置（15,15），长和宽分别为15和15
    r = Rectangle(x=15, y=15, width=15, height=15)
    r.string()
    # 实例化Rectangle对象，顶点位置（40,30），长和宽分别为11和14
    r1 = Rectangle(x=40, y=30, width=11, height=14)
    r1.string()
