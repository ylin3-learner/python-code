# coding:utf-8

# 封裝的例子
class Parent(object):
	def __hello(self, data):
		print('hello %s' % data)
	def helloworld(self):  # 說到“自己”這個詞，都是和相對而言的“其他”而說的
		self.__hello('world') # data = 'world', 在其他函數中調用另一個函數 --私有函數
if __name__ == '__main__':
	p = Parent()
	p.helloworld()
