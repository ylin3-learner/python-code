# coding:utf-8

from .cat.action import run as cat_run # 如果想在包的__init__下導入其它的模塊或模塊, 只要變成.package/func
# from animal import cat_run
# cat_run()

from .dog.action import run as dog_run
# from animal import dog_run
# dog_run()
