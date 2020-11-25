from .CarCamera import CarCamera

class Car:
    def __init__(self, carCamera):
        self.carCamera : CarCamera = carCamera

    def update(self, ms):
        pass

    def finish_iteration(self):
        pass

    def set_right_speed(self, speed):
        pass
    
    def set_left_speed(self, speed):
        pass
        
    def get_image_from_camera(self):
        return self.carCamera.getImage()