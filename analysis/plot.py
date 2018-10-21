import os, sys, csv, re, json

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':

	file = sys.argv[1]
	d = sys.argv[2]
	file = csv.reader(open(file), delimiter=',')

	temp = []

	trending = {}
	overall = {}

	d = os.listdir(d)
	for item in d:
		final = item.replace('tweet-ids_', '').replace('.dat', '')
		temp.append(final)

	for item in file:
		tt = item[0].replace('#', '')

		overall[tt] = 0

		if tt in temp:
			trending[tt] = 0

	print("UNIQUE TRENDING : %s" % len(trending))
	print("UNIQUE OVERALL : %s" % len(overall))







