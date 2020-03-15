#方法一
"""
1.导入
import 包名.模块名
2.调用功能
包名.模块名.功能（）
"""
#方法一
# import myPackage.my_module1
# myPackage.my_module1.info_print()

#方法二 必须在__init__.py文件中添加__all__=[]控制允许导入的模块列表
from myPackage import *
my_module1.info_print()
