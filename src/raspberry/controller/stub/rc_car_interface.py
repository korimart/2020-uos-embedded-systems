class RC_Car_Interface():
    def __init__(self):
        self.left_wheel = 0
        self.right_wheel = 0
        # self.camera = PiCamera()

    def finish_iteration(self):
        print('finish iteration')

    def set_right_speed(self, speed):
        print('set right speed to ', speed)
    
    def set_left_speed(self, speed):
        print('set left speed to ', speed)
        
    def get_image_from_camera(self):
        pass

    def stop(self):     # robot stop
        print('stop')