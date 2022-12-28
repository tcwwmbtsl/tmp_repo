import scrapy


class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanspider'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0']

    def parse(self, response):
        # 解析
        return response.json()
