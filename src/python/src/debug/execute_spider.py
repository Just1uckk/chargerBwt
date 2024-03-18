from scrapy.cmdline import execute

from spiders.charger_shot_spider import ChargerShotSpider

if __name__ == '__main__':
    execute(f"scrapy crawl {ChargerShotSpider.name}".split())

