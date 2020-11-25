from EasyPygame.Components.GameObject import GameObject

class SimulatedCar():
    def __init__(self, carGameObject, width=1):
        self.carGameObject : GameObject = carGameObject
        self.leftSpeed = 0
        self.rightSpeed = 0
        self.width = width

    def update(self, ms):
        pass

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