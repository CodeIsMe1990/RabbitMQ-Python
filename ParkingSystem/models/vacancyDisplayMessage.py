from enum import Enum

class VacancyDisplayMessageType(Enum):
    ENTER = 0
    EXIT = 1

class VacancyDisplayMessage:
    license_plate : str
    timestamp : str
    car_parking_state : VacancyDisplayMessageType
    
    def __init__(self, car_parking_state : VacancyDisplayMessageType):
        self.car_parking_state = car_parking_state