# lambda 语法
- lambda 函数的语法只包含一个语句，表现形式如下：
    lambda [args1,[args2,argsn]]:expression
    其中 lambda 是python的保留关键字，args 和 expression 由用户自定义
    args: 是参数列表
    expression: 是一个参数表达式
# lambda 函数的特性
- lambda 函数是匿名的：
    所谓的匿名函数，就是没有函数名。lambda 函数没有名字
- lambda 函数有输入和输出
    输入是传入到参数列表的值，输出是根据表达式 expression 计算得到值
- lambda 函数拥有自己的命名空间
    不能访问自己参数列表之外或全局命名空间里的参数