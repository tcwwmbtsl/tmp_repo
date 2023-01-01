
def intNum():
    print('开始执行')
    for i in range(5):
        yield i 
        print("继续执行")

num = intNum()

