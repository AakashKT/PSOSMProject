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
import torch, argparse

from model import *

def save_checkpoint(state, filename):
	torch.save(state, filename);

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='PSOSM Projcet : Election tweet classification')
	parser.add_argument('--data_file', type=str, help='Data File')
	parser.add_argument('--save_dir', type=str, help='Model chekpoint saving directory')
	parser.add_argument('--name', type=str, help='Experiment Name')
	parser.add_argument('--epochs', type=int, help='Number of epochs to train')

	args = parser.parse_args()

	data_loader = ElectionDataWithAuxFeatures(args.data_file)
	dataset = DataLoader(data_loader, batch_size=1, num_workers=0, shuffle=True)

	model = ElectionModel(18)
	model.to('cuda:0')
	optimizer = torch.optim.Adam(model.parameters(), lr=0.0001, betas=(0.5, 0.999))

	loss_func = nn.BCELoss()

	print(model)

	for epoch in range(args.epochs):
		total_loss = 0
		for i, item in enumerate(dataset):
			optimizer.zero_grad()

			output = model(item)
			loss = loss_func(output, item['B'])
			loss.backward()
			optimizer.step()

			total_loss += loss.item()

			if i % 1 == 0:
				print('(Epoch : %s) (%s/%s) Loss : %s' % (epoch+1, i+1, len(dataset), loss.item()))
				sys.stdout.flush()

		print('Epoch : %s Loss : %s' % (epoch+1, total_loss))

		if epoch % 5 == 0:
			print('SAVING MODEL AT EPOCH %s' % (epoch+1))
			save_checkpoint({
					'epoch': epoch+1,
					'state_dict':model.state_dict(),
					'optimizer':optimizer.state_dict(),
				}, '%s/%s_%s.pt' % (args.save_dir, args.name, epoch+1))

	save_checkpoint({
			'epoch': args.epochs,
			'state_dict':model.state_dict(),
			'optimizer':optimizer.state_dict(),
		}, '%s/%s_%s.pt' % (args.save_dir, args.name, epoch+1))

		