from ..Car import Car
import time

class RotationalController:
    def __init__(self, car) -> None:
        self.car : Car = car
        self.leftRolling = False
        self.rightRolling = False
    
    def goStraight(self):
        self.leftRolling = True
        self.rightRolling= True
        self.car.set_left_speed(2)
        self.car.set_right_speed(2)
        time.sleep(0.5)
        self.car.set_left_speed(0)
        self.car.set_right_speed(0)
        
    
    def stop(self):
        self.car.set_left_speed(0)
        self.car.set_right_speed(0)

    def goLeft(self, speed):
        self.car.set_left_speed(0)
        self.car.set_right_speed(speed)
        time.sleep(0.5)
        self.car.set_right_speed(0)
        self.car.set_left_speed(0)
   
        
    def goRight(self, speed):
        
        self.car.set_left_speed(speed)
        self.car.set_right_speed(0)
        time.sleep(0.5)
        self.car.set_left_speed(0)
        self.car.set_right_speed(0)        
