from neural.DataLoaderImp.OurDataLoader import OurDataLoader
import numpy as np

loader = OurDataLoader("our-data.npy")
# data = loader.data[18:64]
# np.save("our-data-R90", data)


loader.showDataAsCv2Window()
# X, Y = loader.getTrainingData()

# print(len(X))
# print(len(Y))