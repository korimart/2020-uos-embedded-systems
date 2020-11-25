from EasyPygame.Components import *

from .Car import Car
from .Controller import Controller
from .CarCamera import CarCamera

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.carGameObject: GameObject = None
        self.car: Car = None
        self.controller: Controller = None

    def _requestDependencies(self, dependencyProvider):
        self.carGameObject = GameObject(self, "Car")
        self.car, self.controller = dependencyProvider(self.carGameObject)

    def onLoad(self):
        self.carGameObject.renderComp = DefaultRenderComponent(color=(1, 1, 1))

    def preRender(self, ms):
        self.controller.update(ms)
        self.car.update(ms)

        screenMoveSpeed = 0.01 * ms

        if EasyPygame.isDown("]"):
            self.camera.setDistanceDelta(screenMoveSpeed)

        if EasyPygame.isDown("["):
            self.camera.setDistanceDelta(-screenMoveSpeed)

        if EasyPygame.isDown1stTime("'"):
            self.camera.setDistance(self.camera.DEFAULTDIST)

        if EasyPygame.isDown("w"):
            self.camera.move((0, screenMoveSpeed))

        if EasyPygame.isDown("a"):
            self.camera.move((-screenMoveSpeed, 0))

        if EasyPygame.isDown("s"):
            self.camera.move((0, -screenMoveSpeed))

        if EasyPygame.isDown("d"):
            self.camera.move((screenMoveSpeed, 0))


def start(dependencyProvider):
    """Start a controller with the dependencies provided by
    the DependencyProvider. DependencyProvider is a function
    that takes as the only parameter the GameObject that represents
    the car in the simulation and returns Car and Controller.

    Parameters
    ----------
    dependencyProvider : function
        -- Described above.
    """

    EasyPygame.initWindow(500, 500, "Controller Window", 60)
    EasyPygame.nextSceneOnInit("MainScene", "_requestDependencies", (dependencyProvider, ))
    EasyPygame.loadScene("MainScene")
    EasyPygame.switchScene("MainScene")
    EasyPygame.run()