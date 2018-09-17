# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ZhiboItem(scrapy.Item):
    # {
    #     "id": "36942",
    #     "guid": "abeba116-b9b7-11e8-9339-525400ccac43",
    #     "userId": "89023",
    #     "title": "奥原希望 vs 马琳(蔡赟 苏木解说) 世界羽联日本公开赛女单决赛",
    #     "videourl": "http://1252040487.vod2.myqcloud.com/8bdce988vodtransgzp1252040487/cc3ebb765285890781861803747/v.f30.mp4?t=5b9f6a93&us=69999&sign=d5e7adc3b47e34f8de66607e257c2452",
    #     "imgurl": "http://1252040487.vod2.myqcloud.com/8bdce988vodtransgzp1252040487/cc3ebb765285890781861803747/snapshot/1537105916_2188918815.100_1491300.jpg",
    #     "cate": "体育视频,羽毛球",
    #     "playcount": "1110",
    #     "attcount": "3",
    #     "commentcount": "0",
    #     "status": "1",
    #     "videoStatus": "1",
    #     "insertTime": "1537105914",
    #     "dealTime": "1537106435",
    #     "iP": "210.12.80.209",
    #     "tag": "奥原希望 马琳 蔡赟 苏木 日本公开赛 羽毛球",
    #     "isAsyn": "0",
    #     "totalTimes": "4971",
    #     "isDel": "0",
    #     "isShow": "1",
    #     "intro": "",
    #     "width": "1280",
    #     "height": "720",
    #     "minImgurl": "/uploads/new_upload/video/36942/1537105916_2188918815_min.100_1491300_min.jpg",
    #     "source": "1"
    # }
    id = Field()
    guid = Field()
    useId = Field()
    title = Field()
    videourl = Field()
    imgurl = Field()
    cate = Field()
    playcount = Field()
    attcount = Field()
    commentcount = Field()
    status = Field()
    videoStatus = Field()
    insertTime = Field()
    dealTime = Field()
    iP = Field()
    tag = Field()
    isAsyn = Field()
    totalTimes = Field()
    isDel = Field()
    intro = Field()
    width = Field()
    height = Field()
    minImgurl = Field()
    source = Field()
    pass
