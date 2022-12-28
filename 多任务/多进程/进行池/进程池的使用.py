import time 
from multiprocessing.dummy import Pool

def get_page():
    print("正在下载")
    time.sleep(2)
    print("下载成功")
    
name_list = ['xiaozi', 'aa', 'bb', 'cc']

# 实例化一个进程池对象
pool = Pool(4)
# 将列表中每一个列表传递给 get_page 进行处理
pool.map(get_page, name_list)
    