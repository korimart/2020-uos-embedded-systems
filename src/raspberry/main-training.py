from neural import DataLoader
from neural import Model
import numpy as np

# import dependencies
from neural.DataLoaderImp.GivenDataLoader import GivenDataLoader
from neural.ModelImp.GivenModel import GivenModel
from neural.ModelImp.OurModel import OurModel
from neural.DataLoaderImp.OurDataLoader import OurDataLoader

def combineData(dataList):
    ret = None

    for data in dataList:
        if ret is None:
            ret = data
        else:
            ret = np.append(ret, data, axis=0)

    return ret

if __name__ == "__main__":
    # dependencies
    # dataLoader = GivenDataLoader("trainingdata.p")
    # model = GivenModel()
    model = OurModel()
    # model.load("trained-model2.p")
    dataLoader = OurDataLoader("our-data.npy", ratio=1) # no test set
    dataLoader2 = OurDataLoader("our-data2.npy", ratio=1) # no test set
    dataLoader3 = OurDataLoader("our-data-R90.npy", ratio=1)

    # start of logic
    trainX, trainY = dataLoader.getTrainingData()
    trainX2, trainY2 = dataLoader2.getTrainingData()
    trainX3, trainY3 = dataLoader3.getTrainingData()

    combinedX = combineData([trainX2, trainX, trainX3, trainX3, trainX3])
    combinedY = combineData([trainY2, trainY, trainY3, trainY3, trainY3])
    # combinedX = combineData([trainX, trainX2, trainX3])
    # combinedY = combineData([trainY, trainY2, trainY3])
    # combinedX = combineData([trainX2])
    # combinedY = combineData([trainY2])

    # no validation set for now
    log = model.train(1000, combinedX, combinedY, combinedX, combinedY)
    print(log)

    model.save("trained-model3.p")

    # for i, X in enumerate(trainX):
    #     pred = model.predict(X)
    #     label = trainY[i]
    #     print("[{}] prediction {} label {}".format(i, pred, label))

    #     if i > 10:
    #         break