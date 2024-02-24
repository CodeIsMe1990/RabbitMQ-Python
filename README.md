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


To mount RabbitMQ docker image and start container<br />
(docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management)<br />
Run:
```
py rabbitmq_docker.py
```

To run Parking system correctly
```
py parkingWorker.py [host]
py vacancyBoard.py [host] [parking_lot_id] [slots_total] [slots_occupied]
py parkingEntryMachine.py [host] [parking_lot_id] [license_place]
py parkingExitMachine.py [host] [parking_lot_id] [license_place]
```

Run the worker:
```
py parkingWorker.py localhost
```

Run the Vacancy display boards:
```
py vacancyBoard.py localhost 1 50 0
py vacancyBoard.py localhost 1 50 0
py vacancyBoard.py localhost 2 50 0
```

Emulate entries and exits and see the vacancy displays get updated accordingly
```
py parkingEntryMachine.py localhost 1 ABC123XYZ
py parkingEntryMachine.py localhost 1 ABC124XYZ
py parkingEntryMachine.py localhost 2 ABC125XYZ
py parkingExitMachine.py localhost 1 ABC123XYZ
py parkingEntryMachine.py localhost 2 ABC126XYZ
py parkingEntryMachine.py localhost 1 ABC127XYZ
py parkingExitMachine.py localhost 1 ABC124XYZ
py parkingExitMachine.py localhost 2 ABC125XYZ
py parkingExitMachine.py localhost 2 ABC127XYZ
py parkingExitMachine.py localhost 1 ABC126XYZ
```