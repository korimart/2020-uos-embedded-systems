from learner import DataLoader
from learner import Learner

dataLoader = DataLoader.OriginalDataLoader("trainingdata.p")
learner = Learner.OriginalModel()

trainX, trainY = dataLoader.getTrainingData()
testX, testY = dataLoader.getTestData()

# no validation set for now
learner.train(50, trainX, trainY, trainX, trainY)
learner.save("trained-model.p")

prediction = learner.predict(trainX[0])
label = trainY[0]

print("prediction {} label {}".format(prediction, label))