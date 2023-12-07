# Define here the models for your scraped items
#
# See documentation in:
# https://docs.org/en/latest/topics/items.html

from scrapy import * 


class AticlesItem(Item):
    collection = 'tt_articles'
    id = Field()
    abstract = Field()
    article_url = Field()
    comment_count = Field()
    like_count = Field()
    publish_time = Field()
    source = Field()
    title = Field()
    url = Field()
    user_id = Field()
    created_at = Field()
    crawled_at = Field()