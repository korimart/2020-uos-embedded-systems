from neural.DataLoaderImp.OurDataLoader import OurDataLoader
from neural.ModelImp.OurModel import OurModel
import numpy as np

loader = OurDataLoader("our-data-R90.npy", ratio=1)
model = OurModel()
model.load("trained-model3.p") 

dataX, dataY = loader.getTrainingData()

for i, X in enumerate(dataX):
    category = np.argmax(model.predict(X))
    print("[{}] {}".format(i, category))


loader.showDataAsCv2Window()
# X, Y = loader.getTrainingData()

# print(len(X))
# print(len(Y))