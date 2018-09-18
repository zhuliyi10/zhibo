import codecs
import json
import os

import scrapy


class badminton(scrapy.Spider):
    name = 'badminton'
    url = 'http://v.zhibo.tv/ajax/appnesting/search'
    page = 1
    # custom_settings = {
    #     'cookie': '_csrf=mlZgSDcjdlUJ2eWO_5FpXofvl7ctr8uu; ep=NjA0ODAw; gr_user_id=683efa9b-4eb6-4283-aabd-b1286a8c135d; grwng_uid=fba2b068-c6f4-47c7-8066-60e8d7691e0e; oid=34aac6ea287ac9e9c742aac1be450fc5; sign=b8b7b91f7fe5b69085e42821f3c8b1fe; token=038a0dcf66406659a64f77b5cfa2a3da%2A2883268'
    # }
    cookies = {
        '_csrf': 'mlZgSDcjdlUJ2eWO_5FpXofvl7ctr8uu',
        'grwng_uid': 'fba2b068-c6f4-47c7-8066-60e8d7691e0e',
        'gr_user_id': '683efa9b-4eb6-4283-aabd-b1286a8c135d',
        'token': '038a0dcf66406659a64f77b5cfa2a3da%2A2883268',
        'sign': 'b8b7b91f7fe5b69085e42821f3c8b1fe',
        'ep': 'NjA0ODAw',
        'oid': '34aac6ea287ac9e9c742aac1be450fc5'
    }
    file_path = name + '.csv'

    if not os.path.exists(file_path):
        file = codecs.open(file_path, 'w', 'utf-8')
        file.close()

    first_id = None
    file = codecs.open(file_path, 'r', 'utf-8')
    file.readline()
    first_line = file.readline()
    first_list = first_line.split(',')
    if len(first_list) > 0:
        if first_list[0].isdigit():
            first_id = first_list[0]
    file.close()

    def start_requests(self):
        data = {
            "k": "羽毛球",
            "n": str(self.page),
            "rnd": "0.19737283560050511",
            "_csrf": "WE9xeFlXc1g1IysfChMQMjwjJDJrMiQXB3o3CAE4FS40eBIMK28GLQ=="
        }
        yield scrapy.FormRequest(
            url=self.url,
            formdata=data,
            cookies=self.cookies,
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        json_load = json.loads(response.text)
        list = json_load['data']['list']

        for item in list:
            print(item)
            yield item

        if len(list) > 0:
            last_item = list[-1]
            if not self.first_id or last_item['id'] > self.first_id:
                self.page = self.page + 1
                data = {
                    "k": "羽毛球",
                    "n": str(self.page),
                    "rnd": "0.19737283560050511",
                    "_csrf": "WE9xeFlXc1g1IysfChMQMjwjJDJrMiQXB3o3CAE4FS40eBIMK28GLQ=="
                }
                yield scrapy.FormRequest(
                    url=self.url,
                    formdata=data,
                    cookies=self.cookies,
                    callback=self.parse_detail
                )
            pass
