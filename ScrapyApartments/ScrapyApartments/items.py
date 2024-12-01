# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TayaraItem(scrapy.Item):
    gouvernorat= scrapy.Field()
    delegation= scrapy.Field()
    superficie= scrapy.Field()
    salle_de_bains= scrapy.Field()
    chambres= scrapy.Field()
    prix= scrapy.Field()
    description= scrapy.Field()

