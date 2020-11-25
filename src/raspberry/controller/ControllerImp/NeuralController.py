from ..ICar import ICar

class NeuralController:
    def __init__(self, car) -> None:
        self.car : ICar = car

    def update(self, ms):
        pass