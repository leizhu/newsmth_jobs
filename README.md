# newsmth_jobs
This project uses scrapy to crawl jobs' JD from newsmth(http://www.newsmth.net/nForum/board/Career_Upgrade) 
All the info will be store into [elasticsearch](https://www.elastic.co/products/elasticsearch)

# How to run 
```
cd newsmth_jobs
scrapy crawl newsmth_crawler
```
Now I hard code that when the above cmd execute, 30 latest pages in http://www.newsmth.net/nForum/board/Career_Upgrade will be crawled, the crawled content includes job post_title/post_date/JD-content.

# Elasticsearch(2.x) config
[elasticsearch-py](http://elasticsearch-py.readthedocs.io/en/master/index.html) is used as es client. You can install it(version elasticsearch>=2.0.0,<3.0.0) via
```
pip install elasticsearch
```
You can edit "newsmth_jobs/pipelines.py" tp specify the es config
