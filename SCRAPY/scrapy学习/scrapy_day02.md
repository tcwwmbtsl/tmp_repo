- 创建一个工程： scrapy startproject xxPro
- 在 spiders 子目录中创建一个爬虫文件
    - scrapy genspider spiderName www.xxx.com
- 执行工程：
    - scrapy crawl spiderName
    加参数 --nolog 不打印日志

settings.py ： 
LOG_LEVEL  设置日志等级

- scrapy 持久化存储
    - 基于终端指令
        - 要求： 只可以将 parse 方法的返回值存储不对劲本地的文本文件中
        - 注意：持久化存储对应的文本文件类型
        - 指令：scrapy crawl xxx -o filepath
        - 好处：简介高效便捷
        - 缺点：局限性强，数据只可以存储到指定的文件类型中
    - 基于管道
        - 编码流程：
            - 数据解析
            - 在 item 类中定义相关的属性
            - 将解析的数据封装存储到item类型对象
            - 将 item 类型的对象提交给管道进行持久化存储
            - 在管道类的 process_item 中要将其接受到的 item 对象中存储的数据进行持久化存储操作
            - 在配置文件中开启管道
        - 优点：
            - 通用性强
面试题：将爬取到的数据一份存储到本地一份存储到数据库，如何实现
    - 管道文件中一个管道类对应的是将数据存在到一种平台
    - 爬虫文件提交的item 只会给管道文件中第一个被执行的管道类接受
    - process_item 中的 return item 表示将item 传递给下一个即将被执行的管道类
    