import torch, os, sys, cv2, json
import torch.nn as nn
from torch.nn import init
import functools
import torch.optim as optim

from torch.utils.data import Dataset, DataLoader
from torch.nn import functional as func
from PIL import Image

import torchvision.transforms as transforms
import numpy as np 
import torch


class ElectionDataWithAuxFeatures(Dataset):

	def __init__(self, data_file):
		super(ElectionDataWithAuxFeatures, self).__init__()

		f = open(data_file)
		self.tweets = json.load(f)

	def __len__(self):
		return len(self.tweets)

	def __getitem__(self, index):
		tweet_obj = self.tweets[index]
		tweet_features = tweet_obj['tweet_features'][:]

		tf = tweet_obj['tweet_data']
		tweet_features.append(int(tf['retweet_count']))
		tweet_features.append(int(tf['favourite_count']))
		tweet_features.append(int(tf['created_at']))

		tf = tweet_obj['user']
		tweet_features.append(int(tf['followers_count']))
		tweet_features.append(int(tf['statuses_count']))
		tweet_features.append(0 if tf['verified'] == False else 1)
		tweet_features.append(0 if tf['verified'] == False else 1)
		tweet_features.append(int(tf['created_at']))
		tweet_features.append(int(tf['favourites_count']))
		tweet_features.append(int(tf['friends_count']))
		tweet_features.append(int(tf['listed_count']))

		if tweet_obj['label'] == True:
			label = [0, 1]
		else:
			label = [1, 0]

		tweet_features = torch.from_numpy(np.asarray(tweet_features, dtype=np.float))
		label = torch.from_numpy(np.asarray(label, dtype=np.int))

		final_data = {
			'A': tweet_features.type(torch.float).to('cuda:0'),
			'B': label.type(torch.float).to('cuda:0')
		}

		return final_data

class ElectionModel(nn.Module):

	def __init__(self, input_nc):
		super(ElectionModel, self).__init__()

		self.model = nn.Sequential(
				nn.Linear(input_nc, 150),
				nn.ReLU(),
				nn.Linear(150, 150),
				nn.ReLU(),
				nn.Linear(150, 100),
				nn.ReLU(),
				nn.Linear(100, 100),
				nn.ReLU(),
				nn.Linear(100, 50),
				nn.ReLU(),
				nn.Linear(50, 10),
				nn.ReLU(),
				nn.Linear(10, 2),
				nn.Sigmoid()
			)

	def forward(self, inp):
		return self.model(inp['A'])