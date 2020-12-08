from neural import DataLoader
from neural import Model
import numpy as np

# import dependencies
from neural.DataLoaderImp.GivenDataLoader import GivenDataLoader
from neural.ModelImp.GivenModel import GivenModel
from neural.ModelImp.OurModel import OurModel
from neural.DataLoaderImp.OurDataLoader import OurDataLoader

if __name__ == "__main__":
    # dependencies
    # dataLoader = GivenDataLoader("trainingdata.p")
    # model = GivenModel()
    model = OurModel()
    dataLoader = OurDataLoader("our-data.npy", ratio=1) # no test set

    # start of logic
    trainX, trainY = dataLoader.getTrainingData()
    testX, testY = dataLoader.getTestData()

    # no validation set for now
    model.train(50, trainX, trainY, trainX, trainY)
    model.save("trained-model.p")

    prediction = model.predict(trainX[0])
    prediction = np.around(prediction)

    label = trainY[0]

    print("prediction {} label {}".format(prediction, label))