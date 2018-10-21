from twython import Twython as t
from datastore import *
from bson.objectid import ObjectId

import os, sys, json, time

auth = DataStore('twitter_auth')
auth.work_on('tokens')

handle_datastore = None

def get_twitter_object():
	app_key = auth.get({'_id' : ObjectId('5b844c6eaccb0be087178c98')})
	app_key = app_key[0]['APP_KEY']

	app_secret = auth.get({'_id' : ObjectId('5b844c94accb0be087178c99')})
	app_secret = app_secret[0]['APP_SECRET']

	access_token = auth.get({'_id' : ObjectId('5b844cbeaccb0be087178c9a')})
	access_token = access_token[0]['ACCESS_TOKEN']

	try:
		twitter = t(app_key, access_token=access_token)
		return twitter
	except:
		twitter = t(app_key, app_secret, oauth_version=2)
		access_token = twitter.obtain_access_token()

		auth.update({'_id' : ObjectId('5b844cbeaccb0be087178c9a')}, \
						{'ACCESS_TOKEN' : access_token})

		return get_twitter_object()


def search(tobj, ids):
	return tobj.lookup_status(id=ids, incliude_entities=True)



if __name__ == '__main__':
	tweet_ids_dir = sys.argv[1]
	tweet_ids_items = os.listdir(tweet_ids_dir)

	twitter = get_twitter_object()
	hash_datastore = DataStore('hash_tags')

	for item in tweet_ids_items:
		print(item)
		hash_datastore.work_on(item)
		file = open('%s/%s' % (tweet_ids_dir, item))

		arr = []
		for line in file:
			id_int = int(float(line.replace('\n', '')))
			arr.append(str(id_int))
		
		count = 0
		while True:
			if count+100 > len(arr):
				break

			final = arr[count:count+100]

			tweets = search(twitter, final)
			for i in tweets:
				hash_datastore.put(i)

			count += 100

		file.close()

			


