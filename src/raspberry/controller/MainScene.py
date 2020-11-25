from .KeyboadController import KeyboardController
import EasyPygame
from EasyPygame.Components import *
from OpenGL.GL import *
from .KeyboadController import KeyboardController
from .SimulatedCar import SimulatedCar

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.carGameObject = None
        self.carSim = None
        self.driver = None

    def onLoad(self):
        self.carGameObject = GameObject(self, "Car")
        self.carGameObject.renderComp = DefaultRenderComponent(color=(1, 1, 1))
        self.carSim = SimulatedCar(self.carGameObject)
        self.driver = KeyboardController(self.carSim)

    def preRender(self, ms):
        self.driver.update(ms)
        self.carSim.update(ms)