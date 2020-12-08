from neural.DataLoaderImp.OurDataLoader import OurDataLoader
from neural.ModelImp.OurModel import OurModel
import numpy as np
import cv2

categoryLabel = { 0: "Straight", 1: "Left", 2: "Right" }

# loader = OurDataLoader("our-data-R90.npy", ratio=1)
loader = OurDataLoader("our-data2.npy", ratio=1)
# loader = OurDataLoader("our-data.npy", ratio=1)
model = OurModel()
model.load("trained-model-loss-0.05.p") 

dataX, dataY = loader.getTrainingData()

cv2.namedWindow('Data View')

for i, data in enumerate(dataX):
    image = data.astype("uint8").reshape(16, 16)
    category = np.argmax(model.predict(data))

    print("[{}]\n\thuman: {}\n\tmachine: {}".format(i, categoryLabel[np.argmax(dataY[i])], categoryLabel[category]))

    cv2.imshow("Data View", cv2.resize(image, dsize=(280,280)))
    cv2.waitKey(0)

cv2.destroyAllWindows()