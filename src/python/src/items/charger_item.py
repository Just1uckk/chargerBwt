import scrapy

from rmq.items import RMQItem


class ChargerItem(RMQItem):
    number = scrapy.Field()
    address = scrapy.Field()
    connectors = scrapy.Field()
