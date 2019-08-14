#-*- coding: UTF-8 -*-
import scrapy
class simpleUrl(scrapy.Spider):
    name = "simpleUrl"
    start_urls = [
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/'
    ]
    def parse(self, response):
        #print(response.css('title::text').extract_first())
        page = response.url.split("/")[-2]
        filename = 'mingyanurl-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('开始保存文件：%s' % filename)