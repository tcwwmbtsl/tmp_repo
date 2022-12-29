# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class DoubanPipeline:
    # 用来处理 item 类型对象
    # 该方法可以接收爬虫文件中的item对象
    # 该方法每接收到一个item 就会被调用一次
    fp = None
    # 重写一个父类的一个方法，该方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('./douban.txt', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        content = item['content']
        self.fp.write(content)
        return item
    
    def close_spider(self, spider):
        print("结束爬虫")
        self.fp.close()
        
        
# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class mysqlPipleLine():
    conn = None
    cursor = None
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port='3306', user='root', password='1454015651@DS', db='leixin')
    
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into leixin valuses()')
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()    
        
        
