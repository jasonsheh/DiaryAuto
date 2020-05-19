#!/usr/bin/python
# __author__ = 'JasonSheh'
# __email__ = 'qq3039344@gmail.com'
# -*- coding:utf-8 -*-


import requests


class TodayWeather:
    def __init__(self, result=None):
        if result is None:
            result = {}
        self.city_code = '101190101'  # 南京
        self.api_url = "http://t.weather.sojson.com/api/weather/city/{}".format(self.city_code)
        self.result = result

    def weather(self):
        r = requests.get(self.api_url)
        result = r.json()
        self.result['CITY'] = result['cityInfo']['city']
        self.result['SHIDU'] = result['data']['shidu']
        self.result['PM25'] = result['data']['pm25']
        self.result['PM10'] = result['data']['pm10']
        self.result['HIGH'] = result['data']['forecast'][0]['high']
        self.result['LOW'] = result['data']['forecast'][0]['low']
        self.result['TYPE'] = result['data']['forecast'][0]['type']

        return self.result


if __name__ == '__main__':
    w = TodayWeather().weather()
    print(w)
