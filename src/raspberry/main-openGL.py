from EasyPygame.Components.GameObject import GameObject
from controller.MainScene import start

from controller.CarImp.SimulatedCar import SimulatedCar
from controller.ControllerImp.KeyboadController import KeyboardController
from controller.ControllerImp.NeuralController import NeuralController
from controller.CarCameraImp.DataCamera import DataCamera
from neural.DataLoaderImp.GivenDataLoader import GivenDataLoader
from neural.ModelImp.GivenModel import GivenModel


def givenDataSimulation(carGameObject: GameObject):
    """A DependencyProvider that simulates a car with
    the model given in the lecture."""

    model = GivenModel()
    model.load("trained-model.p")

    carCam = DataCamera(GivenDataLoader("trainingdata.p"))
    car = SimulatedCar(carCam, carGameObject)
    controller = NeuralController(car, model)

    return car, controller


def keyboardSimulation(carGameObject: GameObject):
    """A DependencyProvider that simulates a car with
    the keyboard input."""

    car = SimulatedCar(None, carGameObject)
    controller = KeyboardController(car)

    return car, controller

if __name__ == "__main__":
    start(givenDataSimulation)
    # start(keyboardSimulation)