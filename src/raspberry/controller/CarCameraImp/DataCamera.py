from ..CarCamera import CarCamera
from neural.DataLoader import DataLoader

class DataCamera(CarCamera):
    def __init__(self, dataLoader : DataLoader) -> None:
        self.data = dataLoader.getDataUnshuffled()
        self.count = 0

    def getImage(self):
        """Streams images from storage.

        Returns
        -------
        NumpyArray | None
            -- None if end of stream is reached.
        """

        if self.count >= len(self.data):
            return None

        ret = self.data[self.count]
        self.count += 1
        return ret