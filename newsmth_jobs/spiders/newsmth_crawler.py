# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import urllib
import logging
import re
import datetime
#logger = logging.getLogger()


class NewsmthCrawlerSpider(Spider):
    name = 'newsmth_crawler'
    allowed_domains = ['newsmth.net']
    #start_urls = ['http://www.newsmth.net/nForum/board/Career_Upgrade?p=1']
    start_urls = []
    for i in range(30):
        url = "http://www.newsmth.net/nForum/board/Career_Upgrade?p=" + str(i+1)
        start_urls.append(url)

    def parse(self, response):
        sel = Selector(response)
        page_url = str(response.url)
        print page_url
        if page_url.find("board/Career_Upgrade") != -1:
            for i in range(30):
                path = '//*[@id="body"]/div[3]/table/tbody/tr[' + str(i+1) + ']'
                job_ele = sel.xpath(path)
                title = job_ele.select('td[2]/a/text()').extract()[0].encode("utf-8")
                date = job_ele.select('td[3]/text()').extract()[0].encode("utf-8")
                date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
                match = date_pattern.match(date)
                if match is None:
                   date = datetime.datetime.today().strftime('%Y-%m-%d')
                job_url = job_ele.select('td[2]/a/@href').extract()[0].encode("utf-8")
                post_id = job_url.split("/")[-1]
                job_url = "http://www.newsmth.net" + job_url + "?title=" + title + "&date=" + date + "&id=" + post_id
                yield Request(job_url, callback=self.parse)
        else:
            params = page_url.split("?")[1]
            title_part = params.split("&")[0]
            date_part = params.split("&")[1]
            id_part = params.split("&")[2]
            title_encode = title_part.split("=")[1]
            post_date = date_part.split("=")[1]
            post_title = urllib.unquote(title_encode)
            post_id = id_part.split("=")[1]
            item = {}
            item["post_title"] = post_title
            content = sel.xpath('//*[@id="body"]/div[3]/div[1]/table/tr[2]/td[2]/p').extract()[0].encode("utf-8")
            item["post_content"] = content
            item["post_date"] = post_date
            item["post_id"] = post_id
            yield item
