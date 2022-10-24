# coding:utf-8


# 1、学生类：
# 类型描述：能够描述学生的学号、姓名、已选课程（默认值为空列表）三项信息

class student(object):
    def __init__(self, name, stu_id):
        self.name = name  # 字符串
        self.stu_id = stu_id  # 字符串
        self.course = []  # 列表

    def course_detail(self):
        return 'Name:{}, Selected:{}'.format(self.name, self.course)

    def add_course(self, cour_info):
        self.course.append(cour_info)

    def show_student_info(self):
        return 'name: {}, s_number: {}'.format(self.name, self.stu_id)


class teacher(object):
    def __init__(self, teacher_name, teacher_id, phone_num):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id
        self.phone_num = phone_num


class all_course(object):
    def __init__(self, course_id, course_name, teacher=None):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher

    def binding(self, teacher):
        if bool(teacher) == True:
            self.teacher = teacher
            return {'課程名稱': f'{self.course_name}', '教師名稱': f'{self.teacher.teacher_name}'}
        else:
            return None
'''
binding()方法中传入的参数teacher是对象，当teacher不为None时，使用”对象名.属性名”获取教师名称
'''


