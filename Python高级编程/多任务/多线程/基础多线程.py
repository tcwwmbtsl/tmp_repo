import threading
import time


# 子线程
def sing():
    for i in range(5):
        print("正在唱歌")


# 子线程
def dance():
    for i in range(5):
        print("正在跳舞")


if __name__ == "__main__":
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    # 启动线程，即让线程开始执行
    # 主线程
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    # 查看线程数
    print(len(threading.enumerate()))
