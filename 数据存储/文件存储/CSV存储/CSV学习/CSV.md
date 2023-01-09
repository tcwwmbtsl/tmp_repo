# CSV 写入
1、首先，使用内置的 open() 函数以写入模式打开文件
2、调用 writer() 函数创建一个 CSV writer 对象
3、利用 CSV writer 对象的 writerrow() 或 writerrows() 方法将数据写入
4、关闭文件