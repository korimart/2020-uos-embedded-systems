from neural.DataLoaderImp.OurDataLoader import OurDataLoader
from neural.DataLoaderImp.GivenDataLoader import GivenDataLoader
from controller.CarCameraImp.DataCamera import DataCamera
from neural.ModelImp.HumanModel import HumanModel
from neural.ModelImp.OurModel import OurModel
from controller.CarImp.NetworkCar import NetworkCar
from controller.ControllerImp.RotationalController import RotationalController
import numpy as np
import cv2

car = NetworkCar()
controller = RotationalController(car)
model = None

modelChoice = int(input("0: human\n1: machine\n"))

if modelChoice == 0:
    model = HumanModel()

elif modelChoice == 1:
    model = OurModel()
    model.load("trained-model3.p") 

try: 
    while True:
        # 16 by 16 uint8 numpy array
        img = car.get_image_from_camera() 

        # flatten 16 by 16 image and convert it to float to feed to model
        img = np.array([np.reshape(img, img.shape[0] ** 2)], dtype=np.float32)
        category = np.argmax(model.predict(img))

        if category == 0:
            controller.goStraight()

        elif category == 1:
            controller.rotateLeft(2)

        elif category == 2:
            controller.rotateRight(2)

        print(category)

except KeyboardInterrupt:
    pass
