"""
面向对象的三大特性
·封装
·继承
·多态
"""
"""
一、多态
多态是指一类事物有多重形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）
定义：多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的的执行效果
好处：调用灵活，有了多态，更容易编写通用的代码，做出通用的程序，以适用需求的不断变化。
实现步骤：
定义父类，并提供公共方法
定义子类，并重写父类的方法
传递子类对象给调用者，可以看到不同子类的执行效果不同

"""
#体验多态
#需求：警务人员和警犬一起工作，警犬分两种：追击犯人和追查毒品，携带不同的警犬，执行不同的工作
#1.定义父类：提供公共方法 警犬和人
class Dog(object):
    def work(self):
        print("指哪打哪....")
class Person(object):
    def work_with_dog(self,dog):
        dog.work()

#2.定义子类：子类重写父类方法
class ArmyDog(Dog):
    def work(self):
        print("追击敌人...")
class DrugDog(Dog):
    def work(self):
        print("追查毒品...")
#3.创建对象，调用不同的功能，传入不同的对象，观察不同的结果


ad = ArmyDog()
dd = DrugDog()
daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)