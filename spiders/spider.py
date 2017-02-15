import scrapy


class NgaSpider(scrapy.Spider):
    name = "NgaSpider"
    host = "http://bbs.ngacn.cc/"
    #爬取的初始页
    start_urls = ["http://bbs.ngacn.cc/thread.php?fid=406"]

    #解析函数
    def parse(self,response):
        print(response.body)
