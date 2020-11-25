from EasyPygame.Components import *
from OpenGL.GL import *

from .ICar import ICar
from .IController import IController

# import dependencies
from .CarImp.SimulatedCar import SimulatedCar
from .ControllerImp.KeyboadController import KeyboardController

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.carGameObject = None
        self.car : ICar = None
        self.controller : IController = None

    def onLoad(self):
        self.carGameObject = GameObject(self, "Car")
        self.carGameObject.renderComp = DefaultRenderComponent(color=(1, 1, 1))

        # inject dependencies
        self.car = SimulatedCar(self.carGameObject)
        self.controller = KeyboardController(self.car)

    def preRender(self, ms):
        self.controller.update(ms)
        self.car.update(ms)