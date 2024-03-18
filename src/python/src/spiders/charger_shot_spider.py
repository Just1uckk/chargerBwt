import ast
import json
import scrapy

from items.charger_item import ChargerItem
from rmq.pipelines import ItemProducerPipeline
from rmq.utils import get_import_full_name
from rmq.utils.decorators import rmq_errback, rmq_callback
from scrapy.utils.project import get_project_settings


class ChargerShotSpider(scrapy.Spider):
    name = 'charger_shot_spider'

    custom_settings = {"ITEM_PIPELINES": {get_import_full_name(ItemProducerPipeline): 310}}

    def __init__(self, *args, **kwargs):
        super(ChargerShotSpider, self).__init__(*args, **kwargs)
        self.project_settings = get_project_settings()
        self.result_queue_name = self.project_settings.get("RABBITMQ_CHARGER_RESULTS")

    def get_result_queue_name(self):
        return self.result_queue_name

    def start_requests(self):
        station_list = self.project_settings.get("STATION_LIST")
        try:
            decode_station_list = ast.literal_eval(station_list)
            if len(decode_station_list) != 0:
                form_data = {
                    "numbers": decode_station_list
                }
                headers = {
                    'Content-Type': 'application/json'
                }
                yield scrapy.Request(url="https://api.appflash.top/api/map/get-chunk", method='POST',
                                     headers=headers,
                                     body=json.dumps(form_data),
                                     callback=self.parse)
            else:
                self.logger.error("STATION_LIST empty. Check your .env file.")
                pass
        except Exception:
            self.logger.error("Problem related with .env. Check STATION_LIST row.")
            pass

    @rmq_callback
    def parse(self, response):
        response_body = response.body.decode('utf-8')
        parsed_data = json.loads(response_body)
        for key, station in parsed_data.items():
            item = ChargerItem({
                "number": station["number"],
                "address": station["address"],
                "connectors": station["connectors"]
            })
            yield item

    @rmq_errback
    def _errback_charger_info(self, failure):
        status_code = failure.value.response.status
        description = str(failure.value)
        self.logger.error(f'Code: {status_code}. Description: {description}')
