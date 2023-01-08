import json 
from pathlib import Path

file_path = Path(Path(__file__).parent, 'demo1.js')
data = '[{"姓名":"张三","年龄":"18"},{"姓名":"李四","年龄":"20"}]'
new_data = json.loads(data)
with open(file_path,'w',encoding='utf8') as f2:
    # ensure_ascii=False才能输入中文，否则是Unicode字符
    # indent=2 JSON数据的缩进，美观
    json.dump(new_data,f2,ensure_ascii=False,indent=2)