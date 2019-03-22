import json
json_str='[{"name":"qiyue","age":18,"flag":false},{"name":"qiyue","age":18}]'
student=json.loads(json_str)
print(type(student))
print(student)