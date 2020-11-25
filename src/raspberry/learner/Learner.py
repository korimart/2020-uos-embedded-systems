import torch
import torch.nn as nn
import torch.optim as optim

def training_loop(n_epochs, optimizer, model, lossFunc, trainX, trainY, valiX, valiY):
    log = []

    for epoch in range(n_epochs):
        train_t_p = model(trainX)
        train_loss = lossFunc(train_t_p, trainY)

        # we are not going to call vali_loss.backward() so these return values don't need to
        # inherit the graph that's needed in backpropagation. Let's save memory.
        with torch.no_grad():
            # validation is here just so we can see how the trained model is doing on a separate set of data.
            vali_t_p = model(valiX)
            vali_loss = lossFunc(vali_t_p, valiY)

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        log.append("Epoch {} Train Loss {} Validation Loss {}".format(epoch, train_loss, vali_loss))

        if not torch.isfinite(train_loss).all():
            break

    return "\n".join(log[-10:])


class Learner:
    '''
    Class that hides deep learning libraries from users so the users do
    not need to deal with converting numpy data to the specific objects
    provided by the libraries as in this case to Tensor.
    '''
    
    def __init__(self):
        self.model = None
        self.optimizer = None
        self.lossFunc = None

    def train(self, epoch, trainX, trainY, valiX, valiY):
        trainX = torch.tensor(trainX)
        trainY = torch.tensor(trainY).unsqueeze(1)
        valiX = torch.tensor(valiX)
        valiY = torch.tensor(valiY).unsqueeze(1)
        
        training_loop(epoch, self.optimizer, self.model, self.lossFunc, trainX, trainY, valiX, valiY)

    def predict(self, X):
        with torch.no_grad():
            X = torch.tensor(X)
            Y = self.model(X)

        return Y.numpy()[0]

    def save(self, path):
        torch.save(self.model.state_dict(), path)

    def load(self, path):
        self.model.load_state_dict(torch.load(path))


class OriginalModel(Learner):
    def __init__(self) -> None:
        self.model = nn.Sequential(
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 64),
            nn.ReLU(),
            nn.Linear(64, 1))

        self.optimizer = optim.Adam(self.model.parameters())
        self.lossFunc = nn.MSELoss()