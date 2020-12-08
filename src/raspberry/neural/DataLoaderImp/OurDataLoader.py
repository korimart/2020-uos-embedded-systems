import numpy as np
import cv2
from ..DataLoader import DataLoader

class OurDataLoader(DataLoader):
    ''' TODO
    '''

    def __init__(self, path, seed=0, ratio=3) -> None:
        np.random.seed(seed)

        # original data
        self.data = np.load(path, allow_pickle=True)

        # shuffled data
        data = np.load(path, allow_pickle=True)
        # np.random.shuffle(data)
        imageCount = len(data)
        self.train, self.test = data[0:int(imageCount / ratio)], data[int(imageCount / ratio):]

    @staticmethod
    def _separateDataLabel(loadedData):
        X = np.array([serialized[1] for serialized in loadedData], dtype=np.float32)
        Y = np.zeros(len(loadedData), dtype=np.int)

        for i, data in enumerate(loadedData):
            Y[i] = int(data[0])

        b = np.zeros((Y.size, Y.max() + 1))
        b[np.arange(Y.size),Y] = 1

        return X, b

    def getTrainingData(self):
        return self._separateDataLabel(self.train)

    def getTestData(self):
        return self._separateDataLabel(self.test)

    def showDataAsCv2Window(self):
        cv2.namedWindow('Data View')

        for i, data in enumerate(self.data):
            category = data[0]
            image = data[1]
            image = image.reshape(16, 16)

            print("[{}]".format(i))

            cv2.imshow("Data View", cv2.resize(image, dsize=(280,280)))
            cv2.waitKey(0)

        cv2.destroyAllWindows()
