import os, sys

if __name__ == '__main__':

	input_dir = sys.argv[1]

	items = os.listdir(input_dir)

	for item in items:
		os.system('gunzip -k %s/%s' % (input_dir, item))
