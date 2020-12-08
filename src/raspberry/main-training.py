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
    # testX, testY = dataLoader.getTestData()

    # no validation set for now
    log = model.train(1000, trainX, trainY, trainX, trainY)
    print(log)

    model.save("trained-model.p")

    for i, X in enumerate(trainX):
        pred = model.predict(X)
        label = trainY[i]
        print("[{}] prediction {} label {}".format(i, pred, label))

        if i > 10:
            break