# coding:utf-8

'''
    學生信息庫 -- 批量增, 批量刪除, 批量查, 模糊查找
'''
import json
import os
'''
    面向函數 > 面向對象
'''
'''
    學生信息的持久化 -將信息存入磁盤中保存
    1. 將學生信息存入一個json文件中, 添加讀與寫json的函數
    2. 我們要將用戶添加修改和刪除的行為紀錄到日誌中, 添加與修改都用info代表
       而delete要用warn警告來提示
'''
'''
Studentinfo( )类实例化时需要接收两位参数，实例化时缺少了日志路径参数
在check_user_info( )函数中判断年龄时，是判断age参数是否为int类型，传参时要保持类型一致避免报错
'''
# coding:utf-8

import logging
import json
import os


class NotArgError(Exception):
    def __init__(self, message):
        self.message = message


class MissPathError(Exception):
    def __init__(self, message):
        self.message = message


class FormatError(Exception):
    def __init__(self, message):
        self.message = message


class Studentinfo(object):
    def __init__(self, students_path, log_path):
        self.students_path = students_path
        self.log_path = log_path
        self.log = self.__log()

        self.__init_path()

        self._read()
        print(self.students, '---------')

    def __log(self):
        if os.path.exists(self.log_path):
            mode = 'a'
        else:
            mode = 'w'

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-%(message)s',
            filename = self.log_path,
            filemode=mode
        )
        return logging

    def __init_path(self):  # 判断文件是否正确
        if not os.path.exists(self.students_path):
            raise MissPathError(f'没有相关的地址文件{self.students_path}')

        if not self.students_path.endswith('.json'):
            raise FormatError('当前文件不是json文件')

        if not os.path.isfile(self.students_path):
            raise TypeError('当前的students不是一个文件')

    def _read(self):  # 读取文件
        with open(self.students_path, 'r', encoding='utf-8') as f:
            try:
                data = f.read()
            except Exception as e:
                raise e
        self.students = json.loads(data)

    def __save(self):
        with open(self.students_path, 'w', encoding='utf-8') as f:
            json_data = json.dumps(self.students)
            f.write(json_data)

    def get_by_id(self, student_id):  # 根据学号查询
        return self.students.get(student_id)

    def get_all_students(self):  # 读取数据库内所有的数据
        for id_, value in self.students.items():
            print('学号：{}， 姓名：{}， 年龄：{}，班级：{}，性别：{}'.format(
                id_, value['name'], value['age'], value['class_number'], value['sex']
            ))
        return self.students

    def add(self, **student):  # 添加数据
        try:
            self.check_user_info(**student)
        except Exception as e:
            raise e
        self.__add(**student)
        self.__save()
        self._read()

    def adds(self, new_students):  # 批量添加数据
        for student in new_students:
            try:
                self.check_user_info(**student)
            except Exception as e:
                print(e, student.get('name'))
                continue
            self.__add(**student)

    def __add(self, **student):
        if len(self.students) == 0:
            new_id = 1
        else:
            keys = list(self.students.keys())
            _keys = []
            for item in keys:
                _keys.append(int(item))
            new_id = max(_keys) + 1
        self.students[new_id] = student
        self.log.info('學生%s 被註冊了' % student['name'])


    def deletes(self, ids):  # 批量删除
        for id_ in ids:
            if id_ not in self.students:
                print(f'{id_}不在学生库里面')
                continue
            students_info = self.students.pop(id_)
            print(f'学号{id_} 学生{students_info["name"]}已被删除')
            self.log.warning(f'学号{id_} 学生{students_info["name"]}已被删除')
        self.__save()
        self._read()

    def delete(self, students_id):  # 删除数据
        if students_id not in self.students:
            print('{}并不存在'.format(students_id))
        else:
            user_info = self.students.pop(students_id)
            print('学号是{}，{}同学的信息已被删除'.format(students_id, user_info['name']))
            self.log.warning('学号是{}，{}同学的信息已被删除'.format(students_id, user_info['name']))
        self.__save() # 讀取
        self._read() # 拿到最新數據

    def update_student(self, student_id, **kwargs):  # 更改数据
        if student_id not in self.students:
            print('{}该学号不存在'.format(student_id))
            try:
                self.check_user_info(**kwargs)
            except Exception as e:
                raise e

        self.students[student_id] = kwargs
        self.__save()
        self._read()
        print('同学信息更新完毕')

    def updates(self, updates_student):  # 更改数据并更新
        for students in updates_student:
            try:
                id_ = list(students.keys())[0]
            except IndexError as e:
                print(e)
                continue

            if id_ not in self.students:
                print(f'学号{id_}不存在')
                continue
            user_info = students[id_]
            try:
                self.check_user_info(**user_info)
            except Exception as e:
                print(e)
                continue

            self.students[id_] = user_info
        print('所有用户信息更新完成')
        self.__save()
        self._read()

    def search_users(self, **kwargs):  # 模糊查找

        assert len(kwargs) == 1, '参数数量一次只能传递一个'

        values = list(self.students.values())
        key = None
        value = None
        result = []
        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs['sex']
        elif 'class_number' in kwargs:
            key = 'class_number'
            value = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        else:
            raise NotArgError('没有发现搜索的关键字')

        for user in values:
            if value in user[key]:
                result.append(user)
        return result

    def check_user_info(self, **kwargs):  # 检查数据
        assert len(kwargs) == 4, '参数必须是4个'
        if 'name' not in kwargs:
            raise NotArgError('没有发现学生姓名')
        if 'age' not in kwargs:
            raise NotArgError('没有发现学生年龄')
        if 'class_number' not in kwargs:
            raise NotArgError('没有发现学生班级')
        if 'sex' not in kwargs:
            raise NotArgError('没有发现学生性别')

        name_value = kwargs['name']
        age_value = kwargs['age']
        class_number_value = kwargs['class_number']
        sex_value = kwargs['sex']

        if not isinstance(name_value, str):
            raise TypeError('name应该是字符串类型')
        if not isinstance(age_value, int):
            raise TypeError('age应该是整型')
        if not isinstance(class_number_value, str):
            raise TypeError('class_number应该是字符串类型')
        if not isinstance(sex_value, str):
            raise TypeError('sex应该是字符串类型')


students = {
    1: {
        'name': 'dewei',
        'age': 19,
        'class_number': 'A',
        'sex': 'boy',
    },
    2: {
        'name': '小慕',
        'age': 15,
        'class_number': 'B',
        'sex': 'boy'
    },
    3: {
        'name': '小曼',
        'age': 14,
        'class_number': 'A',
        'sex': 'girl'
    },
    4: {
        'name': '小高',
        'age': 17,
        'class_number': 'A',
        'sex': 'boy'
    },
    5: {
        'name': '小云',
        'age': 16,
        'class_number': 'B',
        'sex': 'girl'
    }
}

stu = Studentinfo('students.json', 'students.log')
# stu.get_all_students()
stu.add(name='dewei', age=15, class_number='a', sex='boy')
print(students)
users = [
    {'name': 'wuyuye', 'age': '18', 'class_number': 'A', 'sex': 'boy'},
    {'name': 'aichenkai', 'age': '19', 'class_number': 'A', 'sex': 'boy'}
]

stu.adds(users)
stu.get_all_students()
stu.updates([
    {1: {'name': 'dewei.zhang', 'age': '18', 'class_number': 'A', 'sex': 'boy'}},
    {2: {'name': 'fuchequn', 'age': '18', 'class_number': 'A', 'sex': 'boy'}}
])

a = stu.search_users(name='小')
print(a)
