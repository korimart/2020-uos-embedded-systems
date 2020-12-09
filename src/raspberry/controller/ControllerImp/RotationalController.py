from ..Car import Car
import time

class RotationalController:
    def __init__(self, car) -> None:
        self.car : Car = car
    
    def goStraight(self):
        self.car.set_left_speed(2)
        self.car.set_right_speed(2)
    
    def rotateLeft(self, speed):
        self.car.set_right_speed(speed)
   
    def rotateRight(self, speed):
        self.car.set_left_speed(speed)