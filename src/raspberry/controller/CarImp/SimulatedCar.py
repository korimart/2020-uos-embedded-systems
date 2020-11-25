import math
import EasyPygame
from EasyPygame.Components.GameObject import GameObject
from EasyPygame.Components.GUI import Text
from ..Car import Car

class SimulatedCar(Car):
    def __init__(self, carCamera, carGameObject, width=2):
        super().__init__(carCamera)

        self.carGameObject : GameObject = carGameObject
        self.leftSpeed = 0
        self.rightSpeed = 0
        self.width = width
        self.faceAngle = 0

        # self.text = Text(self.carGameObject.scene, color=(1, 1, 1))
        # self.text2 = Text(self.carGameObject.scene, color=(1, 1, 1))
        # self.text.transform.translate(-5.5, 5, -3)
        # self.text2.transform.translate(-5.5, 4, -3)

    def update(self, ms):
        leftDist = self.leftSpeed * ms / 1000
        rightDist = self.rightSpeed * ms / 1000

        if math.isclose(leftDist, rightDist):
            self.carGameObject.transform.translate(0, max(leftDist, rightDist), 0)
            return
        
        outer = max(leftDist, rightDist)
        inner = min(leftDist, rightDist)
        theta = (outer - inner) / self.width

        # distance between car position and rotataion axis
        rotDist = outer / theta - self.width / 2
        clockwise = leftDist > rightDist

        if clockwise:
            theta *= -1
            rotDist *= -1

        self.carGameObject.transform.translate(-rotDist, 0, 0)
        self.carGameObject.transform.rotateRadian(theta)
        self.carGameObject.transform.translate(rotDist, 0, 0)
        
    def finish_iteration(self):
        raise NotImplementedError()

    def set_right_speed(self, speed):
        self.rightSpeed = speed
        # self._printSpeeds()
    
    def set_left_speed(self, speed):
        self.leftSpeed = speed
        # self._printSpeeds()

    # def _printSpeeds(self):
    #     text = "right: {0:.4f}".format(self.rightSpeed)
    #     text2 = "left: {0:.4f}".format(self.leftSpeed)
    #     self.text.setText(text)
    #     self.text2.setText(text2)