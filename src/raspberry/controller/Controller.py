from abc import ABC

class Controller(ABC):
    """Controls the car. Use KeyboardController to control the car
    with keyboard.
    """

    def update(self, ms):
        pass