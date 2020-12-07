from ..Controller import Controller
from ..Car import Car
from neural.Model import Model

class NeuralController(Controller):
    def __init__(self, car, model) -> None:
        self.car: Car = car
        self.model: Model = model
        self.elapsed = 0

    def update(self, ms):
        img = self.car.get_image_from_camera()
        if img is None:
            return

        self.elapsed += ms
        if self.elapsed < 100:
            return

        self.elapsed = 0

        pred = self.model.predict(img)
        left = pred[0]
        right = pred[1]
        self.car.set_left_speed(left)
        self.car.set_right_speed(right)