#!/usr/bin/env python
import sys
from parkingMachine import ParkingMachine, ParkingMachineType

host = sys.argv[1]
parking_lot_id = sys.argv[2]
license_plate = sys.argv[3]

ParkingMachine(parking_machine_type= ParkingMachineType.Exit, host= host, parking_lot_id= parking_lot_id).register_car(license_plate= license_plate)

# localhost, 1, ABC123XYZ