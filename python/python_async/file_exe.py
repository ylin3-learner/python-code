# coding:utf-8

from example import student, teacher, all_course

def introduction(str):
    print('*******************{}**************************'.format(str))


def prepare_course():  # 列表

    course_dict = {
    '01': '网络爬虫',
    '02': '数据分析',
    '03': '人工智能',
    '04': '机器学习',
    '05': '云计算',
    '06': '大数据',
    '07': '图像识别',
    '08': 'Web开发'
    }
    course_list = []
    for key, value in course_dict.items():  # 循环遍历字典中的数据，将课程编号和课程姓名传入
        course = all_course(course_id=key, course_name=value)  # 课程类得到课程类的实例，空列表追加每一次的课程类实例
        # all_course(course_id, course_name)
        course_list.append(course)
    return course_list

def create_teacher():  # 列表
    teacher_name = ['张亮', '王朋', '李旭', '黄国发', '周勤', '谢富顺', '贾教师', '杨教师']
    teacher_id = ['T' + str(teacher_id) for teacher_id in range(1, 9)]
    # List Comprehension --以一個特別的方式應用for迴圈，並創造出帶有元素的List
    '''
    arr1 = [i for i in range(10)]
    print(arr1)
    我們要創造一個Listarr1。
    裡面要放什麼? 要放變數i。
    變數i哪裡來? 從後面的for迴圈來
    那for迴圈會從range拿出什麼呢? 是0~9。
    於是我們就得到一個含有0~9的List啦!
    '''
    teacher_phone_num = [str(teacher_phone_num) for teacher_phone_num in range(13301122001, 13301122009)]  # 计数到 stop 结束，但不包括 stop
    Teacher = []

    while teacher_id:
        t = teacher(teacher_name=teacher_name.pop(), teacher_id=teacher_id.pop(), phone_num=teacher_phone_num.pop())  # 如果你不給賦予任何索引給 list.pop()，它將刪除列表的最後一個元素。
        Teacher.append(t)
    return Teacher

def course_to_teacher():
    c_to_t = []
    ls_course = prepare_course()  # 调用课程信息初始化方法，使用变量ls_course接收
    ls_teacher = create_teacher()  # 调用教师信息初始化方法，使用变量ls_teacher接收
    # ls_teacher.reverse()  # 倒叙的每一条教师类信息
    '''
    __main__中已经倒叙过一次，course_to_teacher中无需再倒叙
    '''

    for index_ in range(len(ls_course)):
        teacher_list = ls_teacher[index_]
        # 结合课程信息初始化方法prepare_course=ls.course与遍历的数字
        # 得到课程信息初始化方法列表中的每条课程类实例的value, 如 '网络爬虫', '数据分析'
        # result = each_course.binding(teacher=teacher_list)  # 通过 每条课程类实例 -each_course 去绑定倒叙的每一条教师类信息teacher_list

        result = ls_course[index_].binding(teacher=teacher_list)

        # 因為在binding()內, return f'{self.course_name}, 教師名稱:{self.teacher.teacher_name}'
        c_to_t.append(result)  # 将绑定后的每条数据追加到空列表
        '''
        ls_teacher和ls_course是列表，
        可循环遍历range(len(ls_course))获取列表的下标，ls_course中的每一个元素调用binding()方法
        '''

    return c_to_t

def create_student():
    Student_name = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    Student_name.reverse() # 倒叙的学生姓名(student_name)
    stu_id = [stu_id for stu_id in range(1000, 1008)]
    # student类中使用的参数是stu_id，不是Student_id
    Student = []  # 创建空列表
    '''
    2、Student_name和Student_id是列表，
    student类的init方法中需要传入的参数name和stu_id是字符串，
    student()不能直接传入列表，要取列表中的元素作为参数
    '''
    for i in range(len(Student_name)):
        ls_student = student(name=Student_name[i], stu_id=stu_id[i])
        # 循环遍历学生信息的长度，
        # 将学号与（据效果图所示）倒叙的学生姓名(student_name)传入学生类(student)，
        # 得到学生类的实例(ls_student)，将学生类实例追加至空列表(Student)
        Student.append(ls_student)
    return Student  # 返回追加后的列表

if __name__ == '__main__':
    course_to_teacher()  # 调用课程绑定教师函数
    create_student()  # 调用学生信息初始化函数
    introduction(str='慕课学院（1）班学生信息')  # 调用introduction(str)，传入参数，实现效果图标题一展示
    result = course_to_teacher()
    result.reverse()


    for i in create_student():  # 循环输出学生信息
        print(f'{i.name}, s_number:{i.stu_id}')  # 不確定這樣是否正確? 煩請解惑

    introduction(str='慕课学院（1）班学生信息')


    for i in create_student():  # 循环遍历课程绑定教师函数的长度，为学生初始化信息的每一对象添加绑定老师之后的课程信息
        i.add_course(cour_info=result.pop())  # 遍历学生初始化信息，实现如效果图Name：xxx, Selected：[{‘课程名称’: ‘xxx’, ‘教师名称’: ‘xxx’}]的展示
        print(i.course_detail())

# 有bug但我找不到
