#!/usr/bin/env python
import sys
import pika
import pika.channel
import time
import jsonpickle
import topicHelper
from models.carParkingMessage import CarParkingMessage, CarParkingState
from models.vacancyDisplayMessage import VacancyDisplayMessage, VacancyDisplayMessageType

class ParkingWorker:
    host : str
    connection : pika.BlockingConnection
    channel : any

    channel_vacancy_displays: pika.channel.Channel

    def __init__(self, host : str):
        self.host = host

    def init(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))

        self.channel_vacancy_displays = self.connection.channel()
        self.channel_vacancy_displays.exchange_declare(exchange='direct_logs', exchange_type='direct')

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='task_queue', durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='task_queue', on_message_callback=self.callback)
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        message = body.decode()
        print(f" [x] Received {message}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

        car_parking_message : CarParkingMessage = jsonpickle.decode(message)
        self.handle_car_parking_message(car_parking_message)

    def handle_car_parking_message(self, car_parking_message : CarParkingMessage):
        routing_key = topicHelper.mq_topic_vacancy_display(car_parking_message.parking_lot_id)
        vacancy_board_message_type : VacancyDisplayMessageType
        
        if car_parking_message.car_parking_state == CarParkingState.ENTER:
            vacancy_board_message_type = VacancyDisplayMessageType.ENTER
        elif car_parking_message.car_parking_state == CarParkingState.EXIT:
            vacancy_board_message_type = VacancyDisplayMessageType.EXIT

        vbm = VacancyDisplayMessage(vacancy_board_message_type)

        message = jsonpickle.encode(vbm)
        self.channel_vacancy_displays.basic_publish(
            exchange='direct_logs', routing_key=routing_key, body=message)
        print(f" [x] Sent {routing_key}:{message}")

host = sys.argv[1]
ParkingWorker(host).init()