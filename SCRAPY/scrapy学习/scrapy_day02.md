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