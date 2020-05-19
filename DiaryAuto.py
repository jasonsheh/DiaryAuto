#!/usr/bin/python
# __author__ = 'JasonSheh'
# __email__ = 'qq3039344@gmail.com'
# -*- coding:utf-8 -*-

import os
import re
import datetime
from TodayWeather import TodayWeather
from TodayThings import TodayThings


class DiaryAuto:
    def __init__(self):
        self.today = datetime.datetime.now().strftime("%Y/%m/%d")
        self.month = datetime.datetime.now().strftime("%Y%m")
        self.day = datetime.datetime.now().strftime("%d")
        self.data = {'DATE': self.today, 'RECORD': ''}
        self.template_path = './template.md'

    def create_file_folder(self):
        if not os.path.exists("./result"):
            os.mkdir("./result")
        if not os.path.exists("./result/{}".format(self.month)):
            os.mkdir("./result/{}".format(self.month))

    def get_weather(self):
        self.data = TodayWeather(self.data).weather()

    def get_things(self):
        self.data = TodayThings(self.data).things()

    def output(self):
        keyword_pattern = re.compile('&(.*?)&')
        file_content = ""
        with open('./template.md', 'r', encoding='utf-8') as template_file:
            for each_line in template_file:
                keywords = re.findall(keyword_pattern, each_line)
                for keyword in keywords:
                    each_line = each_line.replace('&' + keyword + '&', str(self.data[keyword]))
                file_content += each_line

        file_name = "./result/{}/{}.md".format(self.month, self.day, self.day)
        with open(file_name, 'w', encoding='utf-8') as diary:
            diary.write(file_content)

    @staticmethod
    def clean_temp():
        with open('./temp.txt', 'w', encoding='utf-8'):
            pass

    def run(self):
        self.create_file_folder()
        self.get_weather()
        self.get_things()
        self.output()
        self.clean_temp()


if __name__ == '__main__':
    DiaryAuto().run()
