# -*- coding: utf-8 -*-
import scrapy
import json


class TagSpider(scrapy.Spider):
    name = 'tag'
    allowed_domains = ['instagram.com']

    def __init__(self, hashtag=''):
        self.hashtag = hashtag
        if hashtag == '':
            self.hashtag = input("Qual a hashtag? ")
        self.start_urls = ["https://www.instagram.com/explore/tags/"+self.hashtag+"/?__a=1"]

    def parse(self, response):
        graphql = json.loads(response.text)
        has_next = graphql['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
        edges = graphql['graphql']['hashtag']['edge_hashtag_to_media']['edges']

        for edge in edges:
            node = edge['node']
            img = node['display_url']
            shortcode = node['shortcode']
            # yield scrapy.Request("https://www.instagram.com/p/"+shortcode+"/?__a=1", callback=self.parse_post)
            yield {
                'img': img
            }

        pass
