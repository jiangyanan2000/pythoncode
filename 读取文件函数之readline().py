#readline()一次读取一行内容
f = open("test.txt")
content = f.readline()
print(f"第一行：{content}")
content2 = f.readline()
print(f"第二行：{content2}")
