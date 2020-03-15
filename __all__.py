"""
如果一个模块文件中有__all__变量，当使用from xxx import * 导入时，只能导入这个列表中的元素。
"""
# import my_module1
from my_module1 import *

testA()
testB()