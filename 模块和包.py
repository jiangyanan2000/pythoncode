"""
目标
·了解模块
·导入模块
·制作模块
·__all__
·包的使用方法
一、模块
python模块，是一个python文件，以.py结尾，包含了python对象定义和python语句。模块能定义函数，类和变量，模块里也能包含可以执行的代码
"""
"""
1.1.导入模块
1.1.1导入模块的方式
·import 模块名
·from 模块名 import 功能名
·from 模块名 import *
·from 模块名 as 别名
·from 模块名 impotr 功能名 as 别名
"""
"""
1.1.2导入方式详解
1.1.2.1 import
·语法
1.导入模块
import 模块名
impopr 模块名1，模块名2
2.调用功能
模块名.功能名（）

"""
#体验

import math
print(math.sqrt(9))
print(dir(math))
