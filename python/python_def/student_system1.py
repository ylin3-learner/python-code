# coding:utf-8

'''
    學生信息庫 -- append, dict.items(), .pop(), if key in dict
'''

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

def check_user_info(**kwargs):
    if 'name' not in kwargs:
        return '沒有發現學生姓名'# 使程序不會繼續往下走
    if 'age' not in kwargs:
        return '缺少學生年齡'
    if 'sex' not in kwargs:
        return '缺少學生性別'
    if 'class_number' not in kwargs:
        return '缺少學生班級'
    return True

def get_all_students():
    for id_, value in students.items():
        print('學號:{}, 姓名:{}, 年齡:{}, 性別:{}, 班級:{}'.format(
            id_, value['name'], value['age'], value['sex'], value['class_number']
        ))
    return students

# get_all_students() # 要返回才能打印

# 學號的增加
def add_student(**kwargs):
    check = check_user_info(**kwargs)
    if check != True:
        print(check)
        return
    id_ = max(students) + 1

    students[id_] = {
        'name': kwargs['name'],
        'age': kwargs['age'],
        'sex': kwargs['sex'],
        'class_number': kwargs['class_number']
    }

# add_students(name='小白', age=19, class_number='A', sex='man')
# get_all_students()

# 學號的刪除
def delete_students(student_id):
    if student_id not in students:
        print('{}並不存在'.format(student_id))
    else:
        user_info = students.pop(student_id)
        print('學號是{}, {}同學的信息已經被刪除了!'.format(student_id, user_info['name']))
# delete_students(1)
# add_student(name='小白', age=19, class_number='A', sex='man')
# get_all_students()

def update_student(student_id, **kwargs):  # 學生的學號不可修改,只能針對學生信息修改
    if student_id not in students:
        print('並不存在這個學號:{}' % student_id)

    check = check_user_info(**kwargs)
    if check != True:
        print(check)
        return

    students[student_id] = kwargs
    print('同學信息更新完畢!')

update_student(1, name='dewei.zhang', age=33, class_number='A', sex='man')
get_all_students()

# 精準查找用戶信息

def get_user_by_id(student_id):
    return students.get(student_id)

print(get_user_by_id(3))

def search_users(**kwargs):
    values = list(students.values()) # 因為用戶信息可能重複, 所以返回列表類型較好
    key = None # 需要知道key, 與對應的value
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
        print('沒有發現搜索的關鍵字!')
        return

    for user in values:  # values == 用戶信息
        if user[key] == value:
            result.append(user)
    return result
print('--------')
users = search_users(sex='woman')
print(users)
