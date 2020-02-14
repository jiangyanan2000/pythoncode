#readlines可以按照行的方式把整个文件中的内容进行一次性的读取，并且返回一个列表，其中每一行数据为一个元素。
f = open("test.txt")
content = f.readlines()
print(content)
f.close()
