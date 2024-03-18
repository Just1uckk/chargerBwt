from database.models.charger import ChargerSlot
from rmq.commands import Consumer
from sqlalchemy.dialects.mysql import insert


class BaseResultsConsumer(Consumer):

    def init_queue_name(self, opts):
        self.queue_name = self.settings.get("RABBITMQ_CHARGER_RESULTS")
        return self.queue_name

    def build_message_store_stmt(self, message_body):
        slot_messages = []
        for slot in message_body['connectors']:
            slot_messages.append(
                {
                    "number": message_body['number'],
                    "address": message_body['address'],
                    "api_address": slot['api_address'],
                    "price": slot['price'],
                    "status": slot['status'],
                    "type": slot['type']
                }
            )
        stmt = insert(ChargerSlot)
        stmt = stmt.values(slot_messages)
        return stmt
