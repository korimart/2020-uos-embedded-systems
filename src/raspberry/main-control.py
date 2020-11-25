from EasyPygame.Components import *
from OpenGL.GL import *

from controller.Car import Car
from controller.Controller import Controller
from controller.CarCamera import CarCamera

# import dependencies
from controller.CarImp.SimulatedCar import SimulatedCar
from controller.ControllerImp.KeyboadController import KeyboardController


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.carGameObject: GameObject = None
        self.car: Car = None
        self.controller: Controller = None
        self.carCam: CarCamera = None

    def onLoad(self):
        self.carGameObject = GameObject(self, "Car")
        self.carGameObject.renderComp = DefaultRenderComponent(color=(1, 1, 1))

        # inject dependencies
        self.car = SimulatedCar(self.carCam, self.carGameObject)
        self.controller = KeyboardController(self.car)

    def preRender(self, ms):
        self.controller.update(ms)
        self.car.update(ms)


if __name__ == "__main__":
    EasyPygame.initWindow(500, 500, "Controller Window", 75)
    EasyPygame.loadScene("MainScene")
    EasyPygame.switchScene("MainScene")
    EasyPygame.run()