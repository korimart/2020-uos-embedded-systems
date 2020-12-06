from ..Car import Car

class KeyboardController:
    def __init__(self, car) -> None:
        self.car : Car = car
        self.leftRolling = False
        self.rightRolling = False

    def onLeftDown(self):
        speed = 0 if self.leftRolling else 1
        self.leftRolling = not self.leftRolling
        self.car.set_right_speed(speed)

    def onRightDown(self):
        speed = 0 if self.rightRolling else 1
        self.rightRolling = not self.rightRolling
        self.car.set_left_speed(speed)