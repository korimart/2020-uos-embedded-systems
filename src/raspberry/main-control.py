from EasyPygame.Components import *

from controller.Car import Car
from controller.Controller import Controller
from controller.CarCamera import CarCamera

# import dependencies
from controller.CarImp.SimulatedCar import SimulatedCar
from controller.ControllerImp.KeyboadController import KeyboardController
from controller.ControllerImp.NeuralController import NeuralController
from controller.CarCameraImp.DataCamera import DataCamera
from neural.DataLoaderImp.GivenDataLoader import GivenDataLoader
from neural.ModelImp.GivenModel import GivenModel


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
        self.carCam = DataCamera(GivenDataLoader("trainingdata.p"))
        self.car = SimulatedCar(self.carCam, self.carGameObject)
        # self.controller = KeyboardController(self.car)
        model = GivenModel()
        model.load("trained-model.p")
        self.controller = NeuralController(self.car, model)

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


if __name__ == "__main__":
    EasyPygame.initWindow(500, 500, "Controller Window", 75)
    EasyPygame.loadScene("MainScene")
    EasyPygame.switchScene("MainScene")
    EasyPygame.run()