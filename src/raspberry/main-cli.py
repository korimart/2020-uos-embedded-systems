# import dependencies
from controller.CarCameraImp.RealCamera import RealCamera
from controller.CarImp.RealCar import RealCar
from controller.CarImp.SimulatedCar import SimulatedCar
from controller.ControllerImp.KeyboadController import KeyboardController
from controller.ControllerImp.NeuralController import NeuralController
from controller.CarCameraImp.DataCamera import DataCamera
from neural.DataLoaderImp.GivenDataLoader import GivenDataLoader
from neural.ModelImp.GivenModel import GivenModel
from time import sleep

def givenDataRealCar(): 
    """A DependencyProvider that actually runs a car with
    the model given in the lecture."""

    model = GivenModel()
    model.load("trained-model.p")

    # carCam = RealCamera()
    carCam = DataCamera(GivenDataLoader("trainingdata.p"))
    car = RealCar(carCam)
    controller = NeuralController(car, model)

    return car, controller

def realDataRealCar(): 
    """A DependencyProvider that actually runs a car with
    the model given in the lecture."""

    model = GivenModel()
    model.load("trained-model.p")

    carCam = RealCamera()
    car = RealCar(carCam)
    controller = NeuralController(car, model)

    return car, controller

if __name__ == "__main__":

    car, controller = realDataRealCar()

    while True:
        car.update(32)
        controller.update(32)
        sleep(0.032)
        
