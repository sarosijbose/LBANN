import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms, datasets

import matplotlib.pyplot as plt  
import numpy as np
import math
import time
import cvxpy as cp
import itertools
import os
import statistics as stat
from scipy.io import savemat, loadmat
import scipy as sp

train = datasets.MNIST('', train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor()
                       ]))

test = datasets.MNIST('', train=False, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor()
                       ]))

trainset = torch.utils.data.DataLoader(train, batch_size=128, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=128, shuffle=True)

total = 0
counter_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for data in trainset:
    Xs, ys = data
    for y in ys:
        counter_dict[int(y)] += 1
        total += 1

print(counter_dict)

for i in counter_dict:
    print(f"{i}: {counter_dict[i]/total*100.0}%")
    
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

for epoch in range(3):
    for data in trainset:
        X, y = data 
        net.zero_grad()  
        output = net(X.view(-1,28*28)) 
        loss = F.nll_loss(output, y)  
        loss.backward()
        optimizer.step()  
    print(loss)
    
# torch.save(net, '/content/drive/MyDrive/Google/mnistemp_weights.pt')
net = torch.load('/content/drive/MyDrive/Google/mnistemp_weights.pt')

correct = total = 0

with torch.no_grad():
    for data in testset:
        X, y = data
        output = net(X.view(-1,784))
        for idx, i in enumerate(output):
            if torch.argmax(i) == y[idx]:
                correct += 1
            total += 1

print("Test Accuracy: ", round(correct/total, 3))

fname = '/content/mnistemp_weights.mat'

weights = []
for param_tensor in net.state_dict():
    tensor = net.state_dict()[param_tensor].detach().numpy().astype(np.float64)

    if 'weight' in param_tensor:
        weights.append(tensor)

data = {'weights': np.array(weights, dtype = np.object)}
savemat(fname, data)

l = []
itermax = 0
for batch_idx, data in enumerate(testset):
    batch, _ = data

    img_pairs = list(itertools.combinations(batch,2))
    for pair in img_pairs:
        x = pair[0]
        f_x = net(x.view(-1, 784))

        y = pair[1]
        f_y = net(y.view(-1, 784))

        num = (f_y - f_x).detach().numpy().astype(np.float64)
        deno = (y - x).detach().numpy().astype(np.float64)
        emp = (np.linalg.norm(num, 2))/(np.linalg.norm(np.squeeze(deno, axis=(0,)), 2))

        if emp >= itermax:
            itermax = emp

    l.append(itermax)
    itermax = 0

print(max(l), min(l))
print(stat.mean(l))

