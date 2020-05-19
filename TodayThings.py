#!/usr/bin/python
# __author__ = 'JasonSheh'
# __email__ = 'qq3039344@gmail.com'
# -*- coding:utf-8 -*-

import requests
from config import rescuetime_key


class TodayThings:
    def __init__(self, result=None):
        if result is None:
            result = {}
        self.api_url = "https://www.rescuetime.com/anapi/data"
        self.result = result

    def things(self):
        r = requests.get(self.api_url, data={'key': rescuetime_key, 'format': 'csv'})
        self.result['THINGS'] = r.text.replace(',', '|')
        self.result['THINGS'] = self.result['THINGS'].replace('\n', '|\n|')
        self.result['THINGS'] = self.result['THINGS'].replace('\n', '\n|---|---|---|---|---|---|\n', 1)
        self.result['THINGS'] = '|'+self.result['THINGS'][:-1]

        # 设置取花费时间最长前20条
        self.result['THINGS'] = '\n'.join(self.result['THINGS'].split('\n')[:21])
        return self.result


if __name__ == '__main__':
    t = TodayThings().things()
    print(t)
