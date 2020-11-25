from controller.KeyboardDriver import KeyboardDriver
import EasyPygame
from EasyPygame.Components import *
from OpenGL.GL import *
from .KeyboardDriver import KeyboardDriver
from .SimulatedCar import SimulatedCar

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.carGameObject = None
        self.carSim = None
        self.driver = None

        self.angle = 90

    def onLoad(self):
        self.carGameObject = GameObject(self, "Car")
        self.carGameObject.renderComp = DefaultRenderComponent(color=(1, 1, 1))
        self.carSim = SimulatedCar(self.carGameObject)
        self.driver = KeyboardDriver(self.carSim)

    def preRender(self, ms):
        self.driver.update(ms)
        self.carSim.update(ms)

        if EasyPygame.isDown1stTime("KP5"):
            self.angle += 90
            self.carGameObject.transform.reset()
            self.carGameObject.transform.rotate(self.angle)
            self.carGameObject.transform.translate(1, 0, 0)