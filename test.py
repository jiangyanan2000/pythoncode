import time
f = open("test1.txt","r",encoding="utf-8")
content = f.readlines()
for i in content:
    print(i)

