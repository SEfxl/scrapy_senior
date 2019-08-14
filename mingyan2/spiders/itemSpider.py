#-*- coding: UTF-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class itemSpider(scrapy.Spider):
    name = "itemSpider"
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        mingyan = response.css('div.quote')
        for v in mingyan:
            text = v.css('.text::text').extract_first()
            author = v.css('.author::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            tags = ','.join(tags)
            filename = '%s-语录.txt' % author
            with open(filename,"a+") as f:
                f.write(text)
                f.write('\n')
                f.write('标签：'+tags)
                f.close()
