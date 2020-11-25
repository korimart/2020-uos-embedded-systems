from abc import ABC
from typing import Tuple


class DataLoader(ABC):
    def getTrainingData(self) -> Tuple:
        """Gets the training data set.

        Returns
        -------
        NumpyArray
            -- A numpy array of numpy arrays of length 256 that represents 16x16 gray-scale pixels.
        NumpyArray
            -- A numpy array of lables.
        """

        pass

    def getTestData(self) -> Tuple:
        """Gets the test data set.

        Returns
        -------
        NumpyArray
            -- A numpy array of numpy arrays of length 256 that represents 16x16 gray-scale pixels.
        NumpyArray
            -- A numpy array of lables.
        """

        pass

    def getDataUnshuffled(self) -> Tuple:
        """Gets the original data set as it was loaded.

        Returns
        -------
        NumpyArray
            -- A numpy array of numpy arrays of length 256 that represents 16x16 gray-scale pixels.
        NumpyArray
            -- A numpy array of lables.
        """

        pass