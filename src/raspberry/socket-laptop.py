from neural.DataLoaderImp.OurDataLoader import OurDataLoader
from neural.DataLoaderImp.GivenDataLoader import GivenDataLoader
from controller.CarCameraImp.DataCamera import DataCamera
from neural.ModelImp.HumanModel import HumanModel
from neural.ModelImp.OurModel import OurModel
from controller.CarImp.NetworkCar import NetworkCar
from controller.ControllerImp.RotationalController import RotationalController
import numpy as np
import cv2

# camera = DataCamera(OurDataLoader("trainingdata.p"))
car = NetworkCar()
controller = RotationalController(car)
# model = HumanModel()
model = OurModel()
model.load("trained-model2.p") 

try: 
    while True:
        img = car.get_image_from_camera() 
        # cv2.imshow("Data View", cv2.resize(img, dsize=(280, 280)))
        # print(img)

        img = np.array([np.reshape(img, img.shape[0] ** 2)], dtype=np.float32)
        category = np.argmax(model.predict(img))

        if category == 0:
            controller.goStraight()

        elif category == 1:
            controller.goLeft(2)

        elif category == 2:
            controller.goRight(2)

        print(category)

        # cv2.destroyAllWindows()

except KeyboardInterrupt:
    pass
