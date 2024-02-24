#!/usr/bin/env python
import pika
import time
import jsonpickle
from enum import Enum
from models.carParkingMessage import CarParkingMessage, CarParkingState

class ParkingMachineType(Enum):
    Entry = 0
    Exit = 1

class ParkingMachine:
    parking_lot_id = 0
    parking_machine_type : ParkingMachineType
    connection : pika.BlockingConnection
    channel : any

    def __init__(self, parking_machine_type : ParkingMachineType, host : str, parking_lot_id: int):
        self.parking_machine_type = parking_machine_type
        self.parking_lot_id = parking_lot_id
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host = host))
        self.channel = self.connection.channel()

    def register_car(self, license_plate: str):
        car_parking_state : CarParkingState
        if self.parking_machine_type == ParkingMachineType.Entry:
            car_parking_state = CarParkingState.ENTER
        elif self.parking_machine_type == ParkingMachineType.Exit:
            car_parking_state = CarParkingState.EXIT

        cpd = CarParkingMessage(parking_lot_id=self.parking_lot_id, license_plate = license_plate, timestamp= time.time(), car_parking_state= car_parking_state)
        message = jsonpickle.encode(cpd)
        self.channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            ))
        print(f" [x] Sent {message}")