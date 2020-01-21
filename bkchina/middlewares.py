# -*- coding: utf-8 -*-
import random


class RandomUserAgentMiddleware():
    def __init__(self, user_agent):
        self.user_agents = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        ua = crawler.settings.get('PC_USER_AGENT')
        return cls(user_agent=ua)

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)

class RandomProxyMiddleware(object):
    def __init__(self, proxies):
        self.proxies = proxies

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(proxies=settings.get('PROXIES'))

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxies
