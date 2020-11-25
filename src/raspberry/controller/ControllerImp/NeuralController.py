from ..Controller import Controller
from ..Car import Car
from neural.Model import Model

class NeuralController(Controller):
    def __init__(self, car, model, camera) -> None:
        self.car : Car = car
        self.model : Model = model
        self.camera = camera

    def update(self, ms):
        img = self.camera.getIamge()
        direction = self.model.predict(img)[0]
        speed = 1

        if direction > 0:
            self.car.set_left_speed(speed)
        elif direction < 0:
            self.car.set_right_speed(speed)
        else:
            self.car.set_left_speed(speed)
            self.car.set_right_speed(speed)
        