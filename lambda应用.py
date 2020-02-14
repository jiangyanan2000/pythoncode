student = [{"name":"rose","age":10},{"name":"jack","age":11},{"name":"lily","age":12}]
student.sort(key=lambda x:x["name"],reverse=True)
print(student)