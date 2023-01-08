from pathlib import Path
import json

file_path = Path(Path(__file__).parent, 'demo.js')

with open(file_path, encoding='utf-8') as f:
    # 加载文件对象
    py_list = json.load(f)
    print(py_list)
    print(type(py_list))