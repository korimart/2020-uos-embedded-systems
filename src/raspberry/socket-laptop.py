from neural.ModelImp.HumanModel import HumanModel
from neural.ModelImp.OurModel import OurModel
from controller.ControllerImp.NeuralController import NeuralController
from controller.CarImp.NetworkCar import NetworkCar
from controller.ControllerImp.RotationalController import RotationalController
import cv2
import numpy as np

img = np.zeros(shape=(280, 280))

car = NetworkCar()
controller = RotationalController(car)
model = HumanModel()
# model = OurModel()
# model.load("trained-model.p")
# controller = NeuralController(car, model)

while True:
    cv2.imshow("Data View", cv2.resize(img, dsize=(280, 280)))
    img = np.array([np.reshape(img, img.shape[0] ** 2)], dtype=np.float32)
    category = model.predict(img)

    if category == 0:
        controller.goStraight()

    elif category == 1:
        controller.goLeft(2)

    elif category == 2:
        controller.goRight(2)

    img = car.get_image_from_camera()
    cv2.destroyAllWindows()