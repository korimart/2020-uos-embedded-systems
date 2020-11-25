from ..Controller import Controller
from ..Car import Car
from neural.Model import Model

class NeuralController(Controller):
    def __init__(self, car, model) -> None:
        self.car: Car = car
        self.model: Model = model

    def update(self, ms):
        img = self.car.get_image_from_camera()
        if img is None:
            return

        direction = self.model.predict(img)

        # calculate left and right wheel speed with direction
        if direction < -1.0:
            direction = -1.0
        if direction > 1.0:
            direction = 1.0
        if direction < 0.0:
            left_speed = 1.0 + direction
            right_speed = 1.0
        else:
            right_speed = 1.0 - direction
            left_speed = 1.0

        self.car.set_right_speed(right_speed)
        self.car.set_left_speed(left_speed)