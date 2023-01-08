import json
# loads 传入一个JSON格式的字符串，解码成python对象
data = '[{"姓名":"张三","年龄":"18"},{"姓名":"李四","年龄":"20"}]'
print(type(data))  #返回<class 'str'>
new_data = json.loads(data)
print(new_data)
print(type(new_data))