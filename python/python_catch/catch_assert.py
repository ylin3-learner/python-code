# coding:utf-8

# assert 判斷一個表達式: 在表達式條件為false的時候觸發異常

# assert expression, message -- expression為bool判斷語句, message:具體的錯誤信息, no return
# assert bool(False), message >> AssertionError: message

# coding:utf-8

'''
    學生信息庫 -- 批量增, 批量刪除, 批量查, 模糊查找
'''
'''
    面向函數 > 面向對象
'''
class NotArgError(Exception): # 定義異常類基本信息 -- derive from Exception, its basic info
    def __init__(self, message):
        self.message = message

class StudentInfo(object):
    def __init__(self, students):
        self.students = students  # students -- 用戶信息, 可以在所有的類中調用

    # 精準查找用戶信息

    def get_by_id(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        for id_, value in self.students.items(): # self.students.items() -- 在所有的類中找到他
            print('學號:{}, 姓名:{}, 年齡:{}, 性別:{}, 班級:{}'.format(
                id_, value['name'], value['age'], value['sex'], value['class_number']
            ))
        return self.students

    # get_all_students() # 要返回才能打印

    # 學號的增加 -- 只有一個學生
    def add(self, **student):
        try:
            check = self.check_user_info(**student) # 變成類函數 # 添加異常捕獲
        except Exception as e:
            raise e# 只有一個學生, 可以允許直接拋錯
        self.__add(**student)

    def adds(self, new_students): # 批量增加
        for students in new_students:
            try:                                 # 添加異常捕獲
                self.check_user_info(**students)
            except Exception as e:
                print(e, students.get('name'))
                continue # 既然不符合要求, 就要暫停不允許繼續執行
            self.__add(**students)

    def __add(self, **student): # 添加新的學號, 把新的學生入庫
        new_id = max(self.students) + 1
        self.students[new_id] = student



    # 學號的刪除
    def delete(self, student_id):
        if student_id not in self.students:
            print('{}並不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('學號是{}, {}同學的信息已經被刪除了!'.format(student_id, user_info['name']))

    # 批量刪除
    def deletes(self, ids): # id_ 要刪除的學號, ids--學號
        for id_ in ids:# id_防止和id混用
            if id_ not in self.students: # 此id_不存在
                print(f'{id_}不存在學生庫中')
                continue # 既然不存在, 就不允許刪除
            student_info = self.students.pop(id_)
            print(f'學號是:{id_} 學生是{student_info["name"]}已被移除')

    def update(self, student_id, **kwargs):  # 學生的學號不可修改,只能針對學生信息修改
        if student_id not in self.students:
            print('並不存在這個學號:{}' % student_id)
        try:                                # 添加異常捕獲
            self.check_user_info(**kwargs)   # 變類函數
        except Exception as e:
            raise e                   # 因為update() -- 只是更新函數, 有異常可以直接拋出
        self.students[student_id] = kwargs
        print('同學信息更新完畢!')

    def updates(self, update_students):  # 批量更新,  update_students -- 要更新的學生, 是一個列表
        for student in update_students: # student -- type:dict => key: 學號, value: 學生信息
            # 因為數據有可能沒有0索引
            try:                                # 添加異常捕獲
                id_ = list(student.keys())[0] # 先拿到同學的學號進行驗證
            except IndexError as e:
                print(e)
                continue # 保證程序可以繼續循環, 避免raise Error
            if id_ not in self.students:
                print(f'學號:{id_}不存在')
                continue # 既然不符合要求, 就要暫停不允許繼續執行

            user_info = student[id_] # 判斷value=學生信息不完整
            try:                            # 添加異常捕獲
                self.check_user_info(**user_info)
            except Exception as e:
                print(e)
                continue # 暫停 -- 除非都滿足, 才往下執行
            self.students[id_] = user_info # user_info -- 添加學生信息
        print('所有用戶信息更新完畢')

    def search_users(self, **kwargs):

        # 因為不管字段再長, 在元素來看也只是len(data)=1
        assert len(kwargs) == 1, '參數數量傳遞錯誤'
        values = list(self.students.values())  # 因為用戶信息可能重複, 所以返回列表類型較好
        key = None  # 需要知道key, 與對應的value
        value = None
        result = []

        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs[key]
        elif 'class_number' in kwargs:
            key = 'class_number'
            value = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        else:
            raise NotArgError('沒有發現搜索的關鍵字!') # 自定義異常類型 -- 打印錯誤信息

        for user in values:  # user=[{'name', 'age', 'sex', 'class_number'}, {}]; user[key] = name
            # print(user[key]) -- 較好判斷value, user[key]的先後順序
            # print(value)
            if value in user[key]: # 模糊查找; value可能不完整, user[key]=name
                result.append(user)
        return result

    def check_user_info(self, **kwargs): # 判斷**kwargs的長度
        assert len(kwargs) == 4, '參數必須是四個'  # assert bool(False), message >> AssertionError: message

        if 'name' not in kwargs: # 是否存在參數
            raise NotArgError('沒有發現學生姓名參數')
        if 'age' not in kwargs:
            raise NotArgError('缺少學生年齡參數')
        if 'sex' not in kwargs:
            raise NotArgError('缺少學生性別參數')
        if 'class_number' not in kwargs:
            raise NotArgError('缺少學生班級參數')

        name_value = kwargs['name'] # 參數類別是否正確 # type(value)
        age_value = kwargs['age']
        sex_value = kwargs['sex']
        class_number_value = kwargs['class_number']

        # isinstance(對比的數據/ value, 目標類型/ class) e.g. isinstance(1, int) vs. issubclass(sub_class, class)

        if not isinstance(name_value, str):
            raise TypeError('name 應該是字符串類型')
        if not isinstance(age_value, int):
            raise TypeError('age 應該是整型')
        if not isinstance(sex_value, str):
            raise TypeError('sex 應該是字符串類型')
        if not isinstance(class_number_value, str):
            raise TypeError('class_number 應該是字符串類型')

students = {
    1: {
        'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'man'
        },
    2: {
        'name': '小木',
        'age': 10,
        'class_number': 'B',
        'sex': 'man'
    },
    3: {
        'name': '小曼',
        'age': 18,
        'class_number': 'A',
        'sex': 'woman'
    },
    4: {
        'name': '小高',
        'age': 18,
        'class_number': 'C',
        'sex': 'man'
    },
    5: {
        'name': '小雲',
        'age': 18,
        'class_number': 'B',
        'sex': 'woman'
    }
}

if __name__ == '__main__':
    stu_info = StudentInfo(students) # self.student = students.dict
    user = stu_info.get_by_id(1)
    stu_info.add(name='dewei', age=34, class_number='A', sex='boy')
    user = [
        {'name': 'xiaoming', 'age': 17, 'class_number': 'B', 'sex': 'boy'},
        {'name': 'xiaohong', 'age': 18, 'class_number': 'C', 'sex': 'girl'}
    ]

    stu_info.adds(user)
    stu_info.get_all_students() # 打印所有信息
    print('-------')
    stu_info.deletes([7, 8])
    stu_info.get_all_students() # 打印所有信息

    stu_info.updates([
        {1: {'name': 'dewei.zhang', 'age': 18, 'class_number': 'A', 'sex': 'boy'}},
        {2: {'name': '小木同學', 'age': 18, 'class_number': 'A', 'sex': 'boy'}}
    ])
    stu_info.get_all_students()

    result = stu_info.search_users(name='d')
    print(result)
    result = stu_info.search_users(name='小')
    print(result)
    print('---------')
    result = stu_info.search_users(name='') # 將返回所有信息
    print(result)
    # 如果想用age模糊查找, type(age) = str




