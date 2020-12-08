import cv2
import numpy as np

class HumanModel:
    def __init__(self) -> None:
        self.memory = []

    def predict(self, X):
        key = cv2.waitKey(0)
        category = None

        if key == ord("w"):
            category = np.array([1, 0, 0])

        elif key == ord("a"):
            category = np.array([0, 1, 0])

        elif key == ord("d"):
            category = np.array([0, 0, 1])

        elif key == ord("o"):
            print("saved memory to file")
            toSave = np.array(self.memory)
            np.save("our-data", toSave)

        elif key == ord("c"):
            print("cleared memory")
            self.memory = []

        return category