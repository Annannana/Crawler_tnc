import requests
from lxml import etree

class City:
    def __init__(self):
        self.cities = self.__get_cities__()

    def __get_cities__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        response = requests.get('https://www.bkchina.cn/restaurant/index.html', headers=headers)
        html = etree.HTML(response.text)
        result = html.xpath('//div[@class="region clearboth"]//li/a/text()')
        return result

if __name__ == '__main__':
    city = City()
    city.__get_cities__()
