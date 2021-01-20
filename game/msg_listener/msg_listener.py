from datetime import datetime
import json

from ..gamedb import GameDB

import pika
# from loguru import logger


class MSGListener():
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.queue_name = 'game_events'

        self.channel.queue_declare(queue=self.queue_name)

        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.callback,
            auto_ack=True)

        # self.db = GameDB()

    def callback(self, ch, method, properties, body):
        body = json.loads(body)
        log_record = self.db.add_gamelog(datetime.fromtimestamp(
            float(body['time'])),
            body['username'],
            body['action_string'],
            body['payload'])
        self.db.commit()
        print(f'Saved: {log_record}')

    def start(self):
        print('Message listener started')
        self.channel.start_consuming()

