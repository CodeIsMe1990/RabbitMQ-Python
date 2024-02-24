from enum import Enum

class CarParkingState(Enum):
    ENTER = 0
    EXIT = 1

class CarParkingMessage:
    parking_lot_id : int
    license_plate : str
    timestamp : str
    car_parking_state : CarParkingState
    
    def __init__(self, parking_lot_id : int, license_plate : str, timestamp : str, car_parking_state : CarParkingState):
        self.parking_lot_id = parking_lot_id
        self.license_plate = license_plate
        self.timestamp = timestamp
        self.car_parking_state = car_parking_state