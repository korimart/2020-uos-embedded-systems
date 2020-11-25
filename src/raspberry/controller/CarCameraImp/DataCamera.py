import cv2
import numpy as np

from ..CarCamera import CarCamera
from neural.DataLoader import DataLoader


class DataCamera(CarCamera):
    def __init__(self, dataLoader: DataLoader) -> None:
        self.dataLoader = dataLoader
        self.data = dataLoader.getDataUnshuffled()
        self.count = 0
        cv2.namedWindow("Data View")
        cv2.moveWindow("Data View", 0, 0)

    def getImage(self):
        """Streams images from storage.

        Returns
        -------
        NumpyArray | None
            -- None if end of stream is reached.
        """

        if self.count >= len(self.data):
            cv2.destroyAllWindows()
            return None

        direction, velocity, numpyArray = self.dataLoader.data[self.count]
        cv2.imshow("Data View", np.array(cv2.resize(numpyArray, (280, 280))))

        ret = self.data[self.count]
        self.count += 1
        return ret