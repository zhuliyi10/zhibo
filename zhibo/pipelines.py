# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs


class ZhiboPipeline(object):
    def open_spider(self, spider):

        self.file = codecs.open(spider.name + '.csv', 'r', 'utf-8')
        self.old = self.file.readlines()
        self.file.close()
        self.file = codecs.open(spider.name + '.csv', 'w', 'utf-8')
        line = 'id' + "," + 'guid' + "," + 'userId' + "," + 'title' + "," + 'videourl' + "," + 'imgurl' + "," + 'cate' + "," + 'playcount' + "," \
               + 'attcount' + "," + 'commentcount' + "," + 'status' + "," + 'videoStatus' + "," + 'insertTime' + "," + 'dealTime' + "," + 'iP' + "," \
               + 'tag' + "," + 'isAsyn' + "," + 'totalTimes' + "," + 'isDel' + "," + 'isShow' + "," + 'intro' + "," + 'width' + "," \
               + 'height' + "," + 'minImgurl' + "," + 'source'
        line += '\r\n'
        self.file.write(line)
        self.first_id=None
        if len(self.old) > 1:
            first_line = self.old[1]
            first_list = first_line.split(',')
            if len(first_list) > 0:
                if first_list[0].isdigit():
                    self.first_id = first_list[0]

    def close_spider(self, spider):
        if len(self.old) > 1:
            for n in range(1, len(self.old)):
                line = self.old[n]
                self.file.write(line)
        self.file.close()

    def process_item(self, item, spider):
        if not self.first_id or item['id'] > self.first_id:
            line = item['id'] + "," + item['guid'] + "," + item['userId'] + "," + item['title'] + "," + item[
                'videourl'] + "," + item['imgurl'] + "," + item['cate'].replace(',', " ") + "," + item[
                       'playcount'] + "," + \
                   item[
                       'attcount'] + "," \
                   + item['commentcount'] + "," + item['status'] + "," + item['videoStatus'] + "," + item[
                       'insertTime'] + "," + item['dealTime'] + "," + item['iP'] + "," + item['tag'] + "," + item[
                       'isAsyn'] + "," \
                   + item['totalTimes'] + "," + item['isDel'] + "," + item['isShow'] + "," + item['intro'] + "," + item[
                       'width'] + "," + item['height'] + "," + item['minImgurl'] + "," + item['source']
            line += '\r\n'
            self.file.write(line)

        return item
