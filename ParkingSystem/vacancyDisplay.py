#!/usr/bin/env python
import sys
import pika
import jsonpickle
import topicHelper
from models.vacancyDisplayMessage import VacancyDisplayMessage, VacancyDisplayMessageType

class VacancyDisplay:
    host: str
    connection : pika.BlockingConnection
    channel: any
    parking_lot_id : int = 0
    slots_total : int = 0
    slots_occupied : int = 0

    def __init__(self, host: str, parking_lot_id : int, slots_total : int, slots_occupied: int):
        self.host = host
        self.parking_lot_id = parking_lot_id
        self.slots_total = slots_total
        self.slots_occupied = slots_occupied

    def display_slots_total(self) -> int:
        return self.slots_total
    
    def display_slots_occupied_total(self) -> int:
        return self.slots_occupied

    def display_slots_vacant_total(self) -> int:
        return int(self.slots_total) - int(self.slots_occupied)
    
    def print_stats(self):
        print(f' Total slots: {self.display_slots_total()}\r\nVacant slots: {self.display_slots_vacant_total()}\r\nOccupied slots: {self.display_slots_occupied_total()}')

    def init(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(
            exchange='direct_logs', queue=queue_name, routing_key=topicHelper.mq_topic_vacancy_display(self.parking_lot_id))
        self.channel.basic_consume(
            queue=queue_name, on_message_callback=self.callback, auto_ack=True)
        self.print_stats()
        print(' [*] Waiting for messages. To exit press CTRL+C')


        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        message : VacancyDisplayMessage = jsonpickle.decode(body)

        if message.car_parking_state == VacancyDisplayMessageType.ENTER:
            self.slots_occupied = int(self.slots_occupied) + 1
        elif message.car_parking_state == VacancyDisplayMessageType.EXIT:
            self.slots_occupied = int(self.slots_occupied) - 1

        self.print_stats()

host = sys.argv[1]
parking_lot_id = sys.argv[2]
slots_total = sys.argv[3]
slots_occupied = sys.argv[4]

# localhost, 1, ABC123XYZ
VacancyDisplay(host= host, parking_lot_id=parking_lot_id, slots_total= slots_total, slots_occupied= slots_occupied).init()