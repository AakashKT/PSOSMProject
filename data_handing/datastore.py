import pymongo, os, sys

class DataStore():

	def __init__(self, database_name):
		self.client = pymongo.MongoClient('mongodb://localhost:27017/')

		self.db = self.client[database_name]
		self.collection = None

	def work_on(self, collection_name):
		self.collection = self.db[collection_name]

	def put(self, data):
		return self.collection.insert_one(data)

	def get(self, query):
		return self.collection.find(query)

	def update(self, query, newval):
		return self.collection.update_one(query, newval)

	def get_all(self):
		return self.collection.find() 

	def close(self):
		self.client.close()