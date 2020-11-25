import pickle
import numpy as np
import cv2
from ..DataLoader import DataLoader

class GivenDataLoader(DataLoader):
    '''
    Data is stored as a numpy array in a picke as follows.

    +-----------+----------+-------------------+
    |     0     |    1     |         2         |
    +-----------+----------+-------------------+
    | Direction | Velocity | 16x16 Numpy Array |
    +-----------+----------+-------------------+

    The numpy array at index 2 contains uint8 grayscales of each pixel.
    '''

    def __init__(self, path, seed=0) -> None:
        np.random.seed(seed)

        # original data
        self.data = pickle.load(open(path, "rb"), encoding="latin1")

        # shuffled data
        data = pickle.load( open( path, "rb" ), encoding="latin1" )
        imageCount = len(data)
        self.test, self.train = data[0:int(imageCount / 3)], data[int(imageCount / 3):]

    @staticmethod
    def _separateDataLabel(loadedData):
        X = np.array([np.reshape(serialized[2], serialized[2].shape[0] ** 2) for serialized in loadedData], dtype=np.float32)
        Y = np.zeros((len(loadedData)), dtype=np.float32)

        for i, data in enumerate(loadedData):
            Y[i] = float(data[0])

        return X, Y
        
    def getTrainingData(self):
        return self._separateDataLabel(self.train)

    def getTestData(self):
        return self._separateDataLabel(self.test)

    def getDataUnshuffled(self):
        X = np.array([np.reshape(serialized[2], serialized[2].shape[0] ** 2) for serialized in self.data], dtype=np.float32)
        return X

    def showDataAsCv2Window(self):
        cv2.namedWindow('Data View')

        for i, direction, velocity, numpyArray in enumerate(self.data):
            print("[{}] dir {} vel {}".format(i, direction, velocity))
            cv2.imshow("Data View", np.array(cv2.resize(numpyArray,(280,280))))
            cv2.waitKey(0)

        cv2.destroyAllWindows()
