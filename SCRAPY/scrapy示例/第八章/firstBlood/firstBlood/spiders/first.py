import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称：就是爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名： 用来限定 urls 列表中哪些 url 可以进行请求发送
    #allowed_domains = ['www.xxx.com']
    # 启始的URL 列表: 该列表中存放的url 会被 scrapy 自动进行请求的发送
    start_urls = ['http://www.baidu.com/', 'https://www.sogou.com']

    #　用作于数据解析： response 表示请求成功后对应的响应对象
    # 调用次数由 starts_urls 的长度决定
    def parse(self, response):
        print(response)
