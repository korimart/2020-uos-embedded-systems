from .SimulatedCar import SimulatedCar
import EasyPygame

class KeyboardDriver:
    def __init__(self, car) -> None:
        self.car : SimulatedCar = car
        self.leftRolling = False
        self.rightRolling = False

    def update(self, ms):
        # if EasyPygame.isDown("KP9"):
            # self.driver.onUp(ms)

        # if EasyPygame.isDown("KP2"):
            # self.driver.onDown(ms)

        if EasyPygame.isDown1stTime("KP6"):
            speed = 0 if self.leftRolling else 1
            self.leftRolling = not self.leftRolling
            self.car.set_right_speed(speed)

        if EasyPygame.isDown1stTime("KP4"):
            speed = 0 if self.rightRolling else 1
            self.rightRolling = not self.rightRolling
            self.car.set_left_speed(speed)

    # def onLeft(self, ms):
    #     pass

    # def onRight(self, ms):
    #     pass

    # def onUp(self, ms):
    #     pass

    # def onDown(self, ms):
    #     pass