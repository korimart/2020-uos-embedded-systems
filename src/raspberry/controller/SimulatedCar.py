import math
from EasyPygame.Components.GameObject import GameObject

class SimulatedCar():
    def __init__(self, carGameObject, width=1):
        self.carGameObject : GameObject = carGameObject
        self.leftSpeed = 0
        self.rightSpeed = 0
        self.width = width
        self.faceAngle = 0

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
    
    def set_left_speed(self, speed):
        self.leftSpeed = speed
        
    def get_image_from_camera(self):
        raise NotImplementedError()