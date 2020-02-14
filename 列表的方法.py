list1 = ["TOM","Lily","rose"]
#append()

#extend()
list2 = ["TOM","Lily","rose"]
list2.extend((1,2,4))
print(list2)
"""
注意：虽然append和extend 都是在后面加入元素，但是有所不同，append是直接在后面加入元素，但是extends是把数据拆开加入。
"""
#insert
list3 = ["tom","lily","rose"]
list3.insert(1,"aaa")
print(list3)
"""
insert更为灵活一些，可以指定加入元素的位置
"""
# del  pop()删除指定下标的数据，如不指定下标，默认删除最后一个
#无论是按照下标还是删除最后一个，pop的函数都会返回这个被删除的元素
#remove(数据)  clear() 清空列表
#逆序 reverse()  排序sort()升序和降序