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

    def showDataAsCv2Window(self):
        cv2.namedWindow('Data View')

        for i, data in enumerate(self.data):
            left = data[0]
            right = data[1]
            image = data[2]

            print("[{}] {} {}".format(i, left, right))
            cv2.imshow("Data View", np.array(cv2.resize(image,(280,280))))
            cv2.waitKey(0)

        cv2.destroyAllWindows()
