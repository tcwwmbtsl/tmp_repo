import tkinter as tk
from PIL import Image
from pathlib import Path



# 创建一个窗口
root = tk.Tk()
# 设置窗口大小。800x300 表示窗口大小，200 200 表示窗口相对位置
root.geometry('800x500+200+200')
# 设置标题
root.title('在线观看电影')
# 设置读取一张图片
file_path = Path(Path(__file__).parent, 'test1.gif')

# im = Image.open(file_path)
img = tk.PhotoImage(file=file_path)
# 布局图片
tk.Label(root, image=img).pack()
# 设置标签框
choose_frame = tk.LabelFrame(root).pack()

tk.Label(choose_frame, text='选择接口:', font=('黑体', 20)).pack()
# 让窗口持续展示
root.mainloop()