from ..Car import Car

class KeyboardController:
    def __init__(self, car) -> None:
        self.car : Car = car
        self.leftRolling = False
        self.rightRolling = False
    
    # TODO
    def update(self, ms):
        pass

    def goStraight(self):
        if not self.leftRolling:
            self.leftRolling = True
            self.car.set_left_speed(1)
        if not self.rightRolling:
            self.rightRolling = True
            self.car.set_right_speed(1)
    
    def stop(self):
        self.leftRolling = False
        self.rightRolling = False
        self.car.set_left_speed(0)
        self.car.set_right_speed(0)

    def goLeft(self):
        self.leftRolling = False
        self.car.set_left_speed(0)

        if not self.rightRolling:
            self.rightRolling = True
            self.car.set_right_speed(1)

    def goRight(self):
        self.rightRolling = False
        self.car.set_right_speed(0)

        if not self.leftRolling:
            self.leftRolling = True
            self.car.set_left_speed(1)