from stub import rc_car_interface

class CarController:
    def __init__(self):
        self.car = rc_car_interface()
        self.leftMoving = False
        self.rightMoving = False
        self.speed = 10
    
    def onUp(self, ms):
        pass

    def onDown(self, ms):
        pass

    def onLeft(self, ms):
        if self.leftMoving:
            return

        self.leftMoving = True
        self.car.set_left_speed(self.speed)

    def onRight(self, ms):
        if self.rightMoving:
            return

        self.rightMoving = True
        self.car.set_right_speed(self.speed)