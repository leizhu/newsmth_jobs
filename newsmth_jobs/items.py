# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsmthJobsItem(scrapy.Item):
    # define the fields for your item here like:
    post_title = scrapy.Field()
    post_content = scrapy.Field()
    post_date = scrapy.Field()
    post_id = scrapy.Field()
