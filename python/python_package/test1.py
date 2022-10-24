# coding:utf-8

# for package(包/文件夾) import module(包中的腳本)

# 包 > 模塊 > 函數
# 同一個級別的也能調用只是要變.package/func

# from animal.cat.action import Cat >> from 包名.子包名.模塊名 import 函數
# 可以用as起別名, 避免因函數重名而覆蓋; 因為python中一切都是對象 >> from animal.cat import action as cat_action
# 或者是 from animal.cat.action import run
# cat = Cat()
# cat.run()

from animal import dog_run # 能夠導入是因為test1 和 animal 是在同一個文件夾下
from animal import cat_run
from animal.cat.action import cat_name

# from .py import func/class


dog_run_result = dog_run()
cat_run_result = cat_run()

print(dog_run_result)
print(cat_run_result)
print(cat_name)
