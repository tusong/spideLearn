"""
https://segmentfault.com/a/1190000008334147?utm_source=sf-similar-article
"""

import re
import scrapy
from scrapy import *
from scrapy.exceptions import *

import json

from myproject.toutiaoItems import AticlesItem

from scrapy.spidermiddlewares.httperror import HttpError


class ToutiaoSpider(Spider):
    name = "toutiao_spider"
    allowed_domains = ["www.toutiao.com"]
    url = "https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_article&token={token}&max_behot_time={max_behot_time}&aid=24&app_name=toutiao_web"
    start_urls = ['MS4wLjABAAAApOspM7AnWqplD9FIBGnhJRfUjFT_msD1KZMfNPBZa-c'] # 爬取入口账号token
    task_set = set(start_urls) # 待爬取集合
    tasked_set = set() # 已爬取集合

    headers={
    "Accept": "",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7": "",
    "Accept-Encoding": "",
    "gzip,": "deflate, br",
    "Accept-Language": "",
    "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6": "",
    "Cache-Control": "",
    "no-cache": "",
    "host":"www.toutiao.com"
    } 

    cookies={
    "ttcid": "5b825568c1144e2d9c58a6f1e7147fb638",
    "csrftoken": "486aa65d4b91d22f6e5de38c5894ed88",
    "ttwid": "1%7CzsAocct-O5arZb-0hdb1bjJ-STTEKNomZXNEmneA6Q0%7C1680756186%7Cfd0f66e3a89677d4752b072c8a11c05d298983153878f56922b6eceb4b34bb7e",
    "tt_webid": "7218792800531138108",
    "_ga": "GA1.1.12220769.1696732456",
    "local_city_cache": "%E4%B8%8A%E6%B5%B7",
    "s_v_web_id": "verify_lngup7hx_USE5O2Vb_E7pL_4TpL_9u8a_P09UxxorktoT",
    "tt_scid": "35gDH2fLhhHKwespX16BfrgyjJOyaWBKw5jZ8jBPqKU-S1K.0yldFL0e5LPtHVnvc081",
    "_ga_QEHZPBE5HH": "GS1.1.1699233116.18.1.1699234478.0.0.0"
}  
    
    def start_requests(self):
        while len(self.task_set) > 0 :
            _id = self.task_set.pop()
            if _id in self.tasked_set:
                raise CloseSpider(reason="已存在该数据 %s "% (_id) )
            self.tasked_set.add(_id)
            info_url = self.url.format(token=_id,max_behot_time=0)
            info_item = AticlesItem()
            print(info_url) 
            yield scrapy.Request(info_url, meta={"_id":_id,"handle_httpstatus_all":True},cookies=self.cookies, headers=self.headers,callback=self.article_parse,errback=self.err_parse)
            
    def article_parse(self, response):
        _id = response.meta['_id']
        result = json.loads(response.text)
        if result.get('message') == 'success':
            data = result.get("data")
            for item in data:
                article_item = AticlesItem()
                field_map = {
                    'abstract': 'abstract', 'article_url': 'article_url', 'comment_count': 'comment_count',
                    'like_count': 'like_count', 
                    'publish_time': 'publish_time', 'source': 'source', 'title': 'title', 'url': 'url',
                    'id': 'id',
                }
                for field, attr in field_map.items():
                    article_item[field] = item.get(attr)
                article_item['user_id']= item.get('user_info').get('user_id')
                yield article_item
            if True==result.get("has_more"):
                 max_behot_time = result.get("next").get("max_behot_time")
                 info_url = self.url.format(token=_id,max_behot_time=max_behot_time)
                 yield scrapy.Request(info_url, meta={"_id":_id,"handle_httpstatus_all":True},cookies=self.cookies, headers=self.headers,callback=self.article_parse,errback=self.err_parse)
            

    def err_parse(self, response):
        print(response) 
        
        



