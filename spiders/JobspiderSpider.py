import scrapy
from bs4 import BeautifulSoup
from spiders.pythonJobs import PythonjobsItem

class JobspiderSpider(scrapy.Spider):
    name = 'jobSpider'
    allowed_domains = ['search.51job.com','jobs.51job.com']
    start_urls = ['http://search.51job.com']