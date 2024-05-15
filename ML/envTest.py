import os
import torch
import torchvision
import torch.nn as nn # neural network
import torch.optim as optim # optimizer
import torch.nn.functional as F
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import MNIST

import matplotlib.pyplot as plt
import lightning as L
