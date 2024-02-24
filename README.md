# RabbitMQ-Python

This repository contains examples of usage & implementation of RabbitMQ

- Simple
- WorkQueues
- PublishSubscribe
- Routing
- Topics
- RPC

and Finally

- **ParkingSystem**<br />
    a custom built example - A parking system that can register cars coming in and out of a parking lot and message the correct vacancy displays.


**Prerequisites**
```
python
docker
```

**Project Dependencies**<br />
pika
```
pip install pika --upgrade
```
jsonpickle
```
jsonpickle - pip install jsonpickle --upgrade
```

To mount RabbitMQ docker image and start container<br />
(docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management)<br />
Run:
```
py rabbitmq_docker.py
```

To run Parking system correctly
```
py parkingWorker.py [host]
py vacancyDisplay.py [host] [parking_lot_id] [slots_total] [slots_occupied]
py parkingEntry.py [host] [parking_lot_id] [license_place]
py parkingExit.py [host] [parking_lot_id] [license_place]
```

Run the worker:
```
py parkingWorker.py localhost
```

Run the Vacancy display boards:
```
py vacancyDisplay.py localhost 1 50 0
py vacancyDisplay.py localhost 1 50 0
py vacancyDisplay.py localhost 2 50 0
```

Emulate entries and exits and see the vacancy displays get updated accordingly
```
py parkingEntry.py localhost 1 ABC123XYZ
py parkingEntry.py localhost 1 ABC124XYZ
py parkingEntry.py localhost 2 ABC125XYZ
py parkingExit.py localhost 1 ABC123XYZ
py parkingEntry.py localhost 2 ABC126XYZ
py parkingEntry.py localhost 1 ABC127XYZ
py parkingExit.py localhost 1 ABC124XYZ
py parkingExit.py localhost 2 ABC125XYZ
py parkingExit.py localhost 2 ABC127XYZ
py parkingExit.py localhost 1 ABC126XYZ
```
Equivalent to:
```
parkingOneEntry = ParkingMachine(parking_machine_type= ParkingMachineType.Entry, host= 'localhost', parking_lot_id= 1)
parkingOneExit = ParkingMachine(parking_machine_type= ParkingMachineType.Exit, host= 'localhost', parking_lot_id= 1)
parkingTwoEntry = ParkingMachine(parking_machine_type= ParkingMachineType.Entry, host= 'localhost', parking_lot_id= 2)
parkingTwoExit = ParkingMachine(parking_machine_type= ParkingMachineType.Exit, host= 'localhost', parking_lot_id= 2)

parkingOneEntry.register_car(license_plate= 'ABC123XYZ')
parkingOneEntry.register_car(license_plate= 'ABC124XYZ')
parkingTwoEntry.register_car(license_plate= 'ABC125XYZ')
parkingOneExit.register_car(license_plate= 'ABC123XYZ')
parkingTwoEntry.register_car(license_plate= 'ABC126XYZ')
parkingOneEntry.register_car(license_plate= 'ABC127XYZ')
parkingOneExit.register_car(license_plate= 'ABC124XYZ')
parkingTwoEntry.register_car(license_plate= 'ABC125XYZ')
parkingTwoEntry.register_car(license_plate= 'ABC127XYZ')
parkingOneExit.register_car(license_plate= 'ABC126XYZ')
```