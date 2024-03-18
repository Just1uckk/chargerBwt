from scrapy.cmdline import execute

if __name__ == '__main__':
    execute(f" scrapy base_results_consumer -m worker".split())
