from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2

from ..CarCamera import CarCamera

class RealCamera(CarCamera):
    def __init__(self) -> None:
        super().__init__()

        self.camera = PiCamera()
        self.camera.resolution = (320, 320)  # set camera resolution to (320, 320)
        self.camera.color_effects = (128, 128)  # set camera to black and white

    def getImage(self):
        img = np.empty((320, 320, 3), dtype=np.uint8)
        self.camera.capture(img, "bgr", use_video_port=True)

        img = img[
            :, :, 0
        ]  # 3 dimensions have the same value because camera is set to black and white
        # remove two dimension data
        #        print(img)

        threshold = int(np.mean(img)) * 0.5
        #        print(threshold)

        # Invert black and white with threshold
        ret, img2 = cv2.threshold(
            img.astype(np.uint8), threshold, 255, cv2.THRESH_BINARY_INV
        )

        img2 = cv2.resize(img2, (16, 16), interpolation=cv2.INTER_AREA)
        #        cv2.imshow("Image", img2)
        #        cv2.waitKey(0)

        return img2