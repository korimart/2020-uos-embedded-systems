from abc import ABC
import torch

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
        print(epoch)

        if not torch.isfinite(train_loss).all():
            break

    return "\n".join(log[-10:])


class Model(ABC):
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
        # TODO: 
        trainX = torch.tensor(trainX)
        # trainY = torch.tensor(trainY).type(torch.LongTensor)
        trainY = torch.tensor(trainY).unsqueeze(1).type(torch.FloatTensor)
        valiX = torch.tensor(valiX)
        valiY = torch.tensor(valiY).unsqueeze(1).type(torch.FloatTensor)
        
        return training_loop(epoch, self.optimizer, self.model, self.lossFunc, trainX, trainY, valiX, valiY)

    def predict(self, X):
        """Predicts the label with this model.

        Parameters
        ----------
        X : NumpyArray
            -- A numpy array of input data.

        Returns
        -------
        NumpyArray
            -- A numpy array of output data.
        """

        with torch.no_grad():
            X = torch.tensor(X)
            Y = self.model(X)

        return Y.numpy()

    def save(self, path):
        torch.save(self.model.state_dict(), path)

    def load(self, path):
        self.model.load_state_dict(torch.load(path))