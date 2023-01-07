#!/usr/bin/env python
# coding=utf-8


# 筛选出 1到10 中的偶数，不包含10
def y(x):
    return x % 2 == 0


z = filter(y, [i for i in range(10)])

for i in z:
    print(i)

# 去掉偶数，保留奇数
print(list(filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 把一个序列中的空字符串删掉，['A','','B',None,'C',' ','a',1,0]
lst = ['A', '', 'B', None, 'C', ' ', 'a', 1, 0]
print(list(filter(lambda x: x and str(x).strip(), lst)))

# 水仙花数，100-999，153= 1**3+5**3+3**3


def f1(x):
    return x == ((x % 10)**3 + (x % 100 // 10)**3 + (x // 100)**3)


print(list(filter(f1, range(100, 1000))))

# 100以内，开平方是整数的数
print(list(filter(lambda x: (x**0.5) % 1 == 0, range(1, 100))))
