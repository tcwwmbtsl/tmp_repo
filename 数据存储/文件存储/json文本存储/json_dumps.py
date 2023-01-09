#!/usr/bin/env python
# coding=utf-8
import json

data = '[{"姓名":"张三","年龄":"18"},{"姓名":"李四","年龄":"20"}]'
lit = json.dumps(data)
print(type(lit))