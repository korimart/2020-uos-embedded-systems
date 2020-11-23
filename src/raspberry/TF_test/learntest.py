import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

outputs = 1

from get_image_data import *

def training_loop(n_epochs, optimizer, model, loss_fn, train_t_u, train_t_c, vali_t_u, vali_t_c):
    log = []

    for epoch in range(n_epochs):
        train_t_p = model(train_t_u)
        train_loss = loss_fn(train_t_p, train_t_c)

        # we are not going to call vali_loss.backward() so these return values don't need to
        # inherit the graph that's needed in backpropagation. Let's save memory.
        with torch.no_grad():
            # validation is here just so we can see how the trained model is doing on a separate set of data.
            vali_t_p = model(vali_t_u)
            vali_loss = loss_fn(vali_t_p, vali_t_c)

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        log.append("Epoch {} Train Loss {} Validation Loss {}".format(epoch, train_loss, vali_loss))

        if not torch.isfinite(train_loss).all():
            break

    print("\n".join(log[-10:]))
    
trX,trY = get_training_data()
teX,teY = get_test_data()

trX = torch.tensor(trX)
trY = torch.tensor(trY)
teX = torch.tensor(teX)
teY = torch.tensor(teY)

print(np.shape(trX)[1])
print(trX.shape)

seed = 0
np.random.seed(seed)
torch.random.manual_seed(seed)

model = nn.Sequential(
    nn.Linear(np.shape(trX)[1], 512),
    nn.ReLU(),
    nn.Linear(512, 64),
    nn.ReLU(),
    nn.Linear(64, 1))

optimizer = optim.Adam(model.parameters())

training_loop(50, optimizer, model, nn.MSELoss(), trX, trY, trX, trY)

Y_prediction = model(teX).detach().numpy()

for i in range(1000):
    label = teY[i]
    pred = Y_prediction[i]
    print("label:{:.2f}, pred:{:.2f}".format(label, pred))


def get_direction(img):
    print(img.shape)
#    img = np.array([np.reshape(img,img.shape**2)])
    ret =  model(np.array([img])).detach().numpy()
    return ret

# Predict direction with single image
dir=get_direction(teX[10])
print(dir[0][0])