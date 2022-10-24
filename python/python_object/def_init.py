# coding:utf-8

# 注：此處全域性的變數名，寫成name，只是為了演示而用
# 實際上，好的程式設計風格，應該寫成gName之類的名字，以表示該變數是Global的變數
name = "whole global name"


class Person:
    name = "class global name"

    def __init__(self, newPersionName):
        # self.name = newPersionName;

        # 此處，沒有使用self.name
        # 而使得此處的name，實際上仍是區域性變數name
        # 雖然此處賦值了，但是後面沒有被利用到，屬於被浪費了的區域性變數name
        name = newPersionName

    def sayYourName(self):
        # 此處，之所以沒有像之前一樣出現：
        # AttributeError: Person instance has no attribute 'name'
        # 那是因為，雖然當前的例項self中，沒有在__init__中初始化對應的name變數，例項self中沒有對應的name變數
        # 但是由於例項所對應的類Person，有對應的name變數,所以也是可以正常執行程式碼的
        # 對應的，此處的self.name，實際上是Person.name
        print('My name is %s' % (self.name)) # -> class global name
        print('name within class Person is actually the global name: %s' % (name))  # -> whole global name
        print("only access Person's name via Person.name=%s" % (Person.name))  # -> class global name


def selfAndInitDemo():
    persionInstance = Person("crifan")
    persionInstance.sayYourName()
    print("whole global name is %s" % (name))  # -> whole global name


###############################################################################
if __name__ == "__main__":
    selfAndInitDemo()