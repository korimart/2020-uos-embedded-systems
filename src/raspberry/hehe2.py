# import torch
# import torch.nn as nn

# loss = nn.CrossEntropyLoss()
# input = torch.randn(3, 5, requires_grad=True)
# target = torch.empty(3, dtype=torch.long).random_(5)
# output = loss(input, target)
# output.backward()

from time import sleep

try:
    while True:
        print("hehe")
        sleep(0.5)

except KeyboardInterrupt:
    print("out")
