from functools import reduce
z = lambda x,y:x+y
y = reduce(z, [i for i in range(10)])
print(y)


# 将列表 [1, 3, 5, 7, 9] 转换为 13579
from functools import reduce
print(reduce(lambda x,y:x*10+y,[1,3,5,7,9]))
