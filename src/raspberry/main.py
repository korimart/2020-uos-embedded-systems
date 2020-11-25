from neural import DataLoader
from neural import Model

if __name__ == "__main__":
    # dependencies
    dataLoader = DataLoader.GivenDataLoader("trainingdata.p")
    model = Model.GivenModel()

    # start of logic
    trainX, trainY = dataLoader.getTrainingData()
    testX, testY = dataLoader.getTestData()

    # no validation set for now
    model.train(50, trainX, trainY, trainX, trainY)
    model.save("trained-model.p")

    prediction = model.predict(trainX[0])
    label = trainY[0]

    print("prediction {} label {}".format(prediction, label))