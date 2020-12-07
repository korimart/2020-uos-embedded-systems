from neural.DataLoaderImp.OurDataLoader import OurDataLoader

loader = OurDataLoader("our-data.npy")
X, Y = loader.getTrainingData()

print(len(X))
print(len(Y))