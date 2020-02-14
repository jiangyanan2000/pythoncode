#read(num),如果传入num表示从文件中读取的数据长度（单位是字节），如果没有num，那么表示读取所有的数据。
f = open("test.txt","r+")
#文件内容如果换行，底层有\n，会有字节占位，导致read()书写参数读取出来的眼睛看到的字节和参数不一样
# print(f.read())
print(f.read(100))
f.close()
