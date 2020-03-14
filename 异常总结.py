"""
异常总结
·异常语法
try:
   可能发生异常的代码
except：
   如果发生异常执行的代码
else:
   没有发生异常执行的代码
finally:
   无论是否发生异常都要执行的代码

·捕获异常
except 异常类型
     代码

except 异常类型 as xx:
     代码

·自定义异常
class 异常类名（Exception）:
      代码
      def __str__(self):
        return ...
·抛出异常
   raise 异常类名（）
 捕获异常
 except Exception...
"""