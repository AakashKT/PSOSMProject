import os, sys, csv, re, json

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':

	##################################
	# Read specific hashtags from json
	##################################

	# file = sys.argv[1]
	# file = json.load(open(file))
	# temp = []

	# for item in file:
	# 	text = item['text']
	# 	hashtags = re.findall('(#[A-Za-z0-9]+)', text)

	# 	for item in hashtags:
	# 		temp.append([item, text])

	# op = csv.writer(open('election_hashtags.csv', 'w+'))
	# op.writerows(temp)



	##################################
	# Read specific hashtags from csv
	##################################

	file = sys.argv[1]
	temp = []

	file = csv.reader(open(file), delimiter=',')

	for row in file:
		text = row[8]
		hashtags = re.findall('(#[A-Za-z0-9]+)', text)
		# print(temp)

		for item in hashtags:
			temp.append([item, text])

	op = csv.writer(open('la_hashtags.csv', 'w+'))
	op.writerows(temp)




	################################
	# Compare with trending hashtags
	################################

	# file = sys.argv[1]
	# d = sys.argv[2]
	# file = csv.reader(open(file), delimiter=',')

	# temp = []

	# # for item in file:
	# # 	temp.append(item[0].replace('#', ''))

	# # d = os.listdir(d)
	# # count = 0
	# # for item in d:
	# # 	final = item.replace('tweet-ids_', '').replace('.dat', '')

	# # 	if final in temp:
	# # 		# print("TRUE")
	# # 		print(final)
	# # 		count += 1

	# d = os.listdir(d)
	# for item in d:
	# 	final = item.replace('tweet-ids_', '').replace('.dat', '')
	# 	temp.append(final)

	# count = 0
	# for item in file:
	# 	tt = item[0].replace('#', '')

	# 	if tt in temp:
	# 		print("HASHTAG : %s , TWEET : %s" % (tt, item[1]))
	# 		count += 1

	# print("NO. OF TAGS %s" % len(d))
	# print("FINAL OVERLAP %s" % count)







