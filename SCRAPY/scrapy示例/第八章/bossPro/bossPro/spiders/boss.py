import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/web/geek/job?query=&page=1']

    def parse(self, response):
        li_list = response.xpath('//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li')
        print(li_list)
        for li in li_list:
            job_name = li.xpath('.//span[@class="job-name"]/text()').extract_first()
            print(job_name)
