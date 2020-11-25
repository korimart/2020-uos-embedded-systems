from EasyPygame.Components.GameObject import GameObject

class SimulatedCar():
    def __init__(self, carGameObject, width=1):
        self.carGameObject : GameObject = carGameObject
        self.left_wheel = 0
        self.right_wheel = 0
        self.width = width

    def update(self, ms):
        dist = self.left_wheel * ms / 1000
        self.carGameObject.transform.translate(0, dist, 0)

    def finish_iteration(self):
        print('finish iteration')

    def set_right_speed(self, speed):
        print('set right speed to ', speed)
        self.right_wheel = speed
    
    def set_left_speed(self, speed):
        print('set left speed to ', speed)
        self.left_wheel = speed
        
    def get_image_from_camera(self):
        pass