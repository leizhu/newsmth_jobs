# -*- coding: utf-8 -*-

import codecs
import json
from elasticsearch import Elasticsearch
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsmthJobsPipeline(object):
    def __init__(self):
        #self.file = codecs.open('newsmth.json', 'wb', encoding='utf-8')
        self.es = Elasticsearch(hosts=[{'host': '172.22.112.251', 'port': 9200}])

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        #self.file.write(line.decode("unicode_escape"))
        ret = self.es.index(index="newsmth", doc_type="post", id=item["post_id"], body=item)
        print ret
        return item
