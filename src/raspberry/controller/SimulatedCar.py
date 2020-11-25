import math
from EasyPygame.Components.GameObject import GameObject

class SimulatedCar():
    def __init__(self, carGameObject, width=1):
        self.carGameObject : GameObject = carGameObject
        self.leftSpeed = 0
        self.rightSpeed = 0
        self.width = width

    def update(self, ms):
        leftDist = self.leftSpeed * ms / 1000
        rightDist = self.rightSpeed * ms / 1000

        if math.isclose(leftDist, rightDist):
            self.carGameObject.transform.translate(0, max(leftDist, rightDist), 0)
        else:
            outer = max(leftDist, rightDist)
            inner = min(leftDist, rightDist)
            theta = (inner - outer) / self.width

            # distance to the x position of the axis of rotation
            rotDist = outer / theta - self.width / 2
            clockwise = leftDist > rightDist
            if clockwise:
                theta *= -1
                rotDist *= -1

            x, y, z = self.carGameObject.transform.getPosition()
            self.carGameObject.transform.reset()

            self.carGameObject.transform.translate(x, y, z)
            self.carGameObject.transform.rotateRadian(theta)
            self.carGameObject.transform.translate(rotDist, 0, 0)
            

    def finish_iteration(self):
        print('finish iteration')

    def set_right_speed(self, speed):
        print('set right speed to ', speed)
        self.rightSpeed = speed
    
    def set_left_speed(self, speed):
        print('set left speed to ', speed)
        self.leftSpeed = speed
        
    def get_image_from_camera(self):
        pass