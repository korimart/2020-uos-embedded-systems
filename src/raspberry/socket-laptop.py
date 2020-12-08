from controller.CarImp.NetworkCar import NetworkCar
import cv2
import numpy as np

car = NetworkCar()

while True:
    command = input("command: ")

    if command == "R":
        car.set_right_speed(2)

    if command == "C":
        img = car.get_image_from_camera()
        img = img.reshape(16, 16)
        cv2.imshow("Data View", np.array(cv2.resize(img,(280,280))))
        cv2.waitKey(0)
        cv2.destroyAllWindows()