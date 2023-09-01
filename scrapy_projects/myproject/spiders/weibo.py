# -*- coding: utf-8 -*-
import scrapy, time
from scrapy.loader import ItemLoader
from myproject.items import SinaUserItem
 
 
class WeiboSpider(scrapy.Spider):
    # 爬虫的名字，唯一标识
    name = 'weibo'
    # 允许爬取的域名范围
    allowed_domains = ['m.weibo.cn']
    # 爬虫的起始页面url
    start_urls = ['https://m.weibo.cn/u/1686546714']
 
    def __init__(self):
        self.headers = {
            'Referer': 'https://m.weibo.cn/u/1686546714',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
 
        self.cookies = {
            
        }
 
    def start_requests(self):
        """
        构造最初 request 函数\n
        :return:
        """
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.base_info_parse, headers=self.headers, cookies=self.cookies)
 
    def base_info_parse(self, response):
        """
        微博用户基本信息解析函数\n
        :param response:
        :return:
        """
        # 加载器（Loader）
        load = ItemLoader(item=SinaUserItem(), response=response)
        selector = scrapy.Selector(response)

        print("response_text:",response.text)

        # 解析微博用户名称  
        re_url = selector.xpath("//span[@class='mod-fil-n']/span")
        user_name = re_url[0] if re_url else ''
        load.add_value('user_name', user_name)

        # 解析微博用户 id
        re_url = selector.xpath('///a[contains(@href,"uid")]/@href').re('uid=(\d{10})')
        user_id = re_url[0] if re_url else ''
        load.add_value('user_id', user_id)
        # 微博数
        webo_num_re = selector.xpath('//div[@class="tip2"]').re(u'微博\[(\d+)\]')
        webo_num = int(webo_num_re[0]) if webo_num_re else 0
        load.add_value('webo_num', webo_num)
        # 关注人数
        follow_num_re = selector.xpath('//div[@class="txt-shadow"]').re(u'关注\[(\d+)\]')
        follow_num = int(follow_num_re[0]) if follow_num_re else 0
        load.add_value('follow_num', follow_num)
        # 粉丝人数
        fans_num_re = selector.xpath('//div[@class="txt-shadow"]').re(u'粉丝\[(\d+)\]')
        fans_num = int(fans_num_re[0]) if fans_num_re else 0
        load.add_value('fans_num', fans_num)
        # 记录爬取时间
        load.add_value('crawl_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        return load.load_item()
