import numpy as np
import cv2
from ..DataLoader import DataLoader

class OurDataLoader(DataLoader):
    ''' TODO
    '''

    def __init__(self, path, seed=0) -> None:
        np.random.seed(seed)

        # original data
        self.data = np.load(path, allow_pickle=True)

        # shuffled data
        data = np.load(path, allow_pickle=True)
        imageCount = len(data)
        self.test, self.train = data[0:int(imageCount / 3)], data[int(imageCount / 3):]

    @staticmethod
    def _separateDataLabel(loadedData):
        X = np.array([np.reshape(serialized[2], serialized[2].shape[0] ** 2) for serialized in loadedData], dtype=np.float32)
        Y = np.zeros((len(loadedData), 2), dtype=np.float32)

        for i, data in enumerate(loadedData):
            Y[i] = float(data[0])

        Y = np.zeros((Y.size, Y.max() + 1))
        Y[np.arange(Y.size), Y] = 1

        return X, Y

    def getTrainingData(self):
        return self._separateDataLabel(self.train)

    def getTestData(self):
        return self._separateDataLabel(self.test)

    def showDataAsCv2Window(self):
        cv2.namedWindow('Data View')

        for i, data in enumerate(self.data):
            category = data[0]
            image = data[1]

            cv2.imshow("Data View", np.array(cv2.resize(image,(280,280))))
            cv2.waitKey(0)

        cv2.destroyAllWindows()
