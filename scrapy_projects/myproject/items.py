# Define here the models for your scraped items
#
# See documentation in:
# https://docs.org/en/latest/topics/items.html

from scrapy import * 


class MyprojectItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class ProfileItem(Item):
    """
    账号的微博数、关注数、粉丝数及详情
    """
    _id = Field()
    nick_name = Field()
    profile_pic = Field()
    tweet_stats = Field()
    following_stats = Field()
    follower_stats = Field()
    sex = Field()
    location = Field()
    birthday = Field()
    bio = Field()
    
class FollowingItem(Item):
    """
    关注的微博账号
    """
    _id = Field()
    relationship = Field()

class FollowedItem(Item):
    """
    粉丝的微博账号
    """
    _id = Field()
    relationship = Field()


class SinaUserItem(Item):
    # 微博用户唯一标识
    user_id = Field()
    # 用户昵称
    user_name = Field()
    # 微博数量
    webo_num = Field()
    # 关注人数
    follow_num = Field()
    # 粉丝人数
    fans_num = Field()
    # 性别
    gender = Field()
    # 地区
    district = Field()
    # 省份
    province = Field()
    # 地市
    city = Field()
    # 生日
    birthday = Field()
    # 简介
    brief_intro = Field()
    # 认证
    identify = Field()
    # 头像 URL
    head_img = Field()
    # 爬取时间
    crawl_time = Field()


class UserItem(Item):
    collection = 'users'
    id = Field()
    name = Field()
    avatar = Field()
    cover = Field()
    gender = Field()
    description = Field()
    fans_count = Field()
    follows_count = Field()
    weibos_count = Field()
    verified = Field()
    verified_reason = Field()
    verified_type = Field()
    follows = Field()
    fans = Field()
    crawled_at = Field()

class UserRelationItem(Item):
    collection = 'users'
    id = Field()
    follows = Field()
    fans = Field()

class WeiboItem(Item):
    collection = 'weibos'
    id = Field()
    attitudes_count = Field()
    comments_count = Field()
    reposts_count = Field()
    picture = Field()
    pictures = Field()
    source = Field()
    text = Field()
    raw_text = Field()
    thumbnail = Field()
    user = Field()
    created_at = Field()
    crawled_at = Field()