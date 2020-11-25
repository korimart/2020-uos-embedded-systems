import torch
import torch.nn as nn
import torch.optim as optim

from ..Model import Model


class GivenModel(Model):
    def __init__(self) -> None:
        self.model = nn.Sequential(
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
        )

        self.optimizer = optim.Adam(self.model.parameters())
        self.lossFunc = nn.MSELoss()