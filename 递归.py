"""
递归的特点：函数自己调用自己，必须要有出口
"""
#需求:求3以内的数的和（用递归算法）

def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num-1)

result = sum_numbers(3)
print(result)