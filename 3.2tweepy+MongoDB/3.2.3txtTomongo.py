from pymongo import MongoClient
# MongoDB api https://api.mongodb.com/python/current/api/pymongo/mongo_client.html
# twFile_list = ["tweets_vogue_live.txt", "tweets_elle_live.txt"]

client = MongoClient()
db = client.pythonbicookbook
files = db.files
f = open('tweets_vogue_live.txt')
text = f.read()
doc = {
"file_name": "tweets_vogue_live.txt",
"contents" : text }
files.insert_one(doc)

# currently, I cannot import the file into mongo DB, because the data is too large.
# client = MongoClient()
# db = client.pythonbicookbook
# files = db.files
# f = open('tweets_elle_live.txt')
# text = f.read()
# doc = {
# "file_name": "tweets_elle_live.txt",
# "contents" : text }
# files.insert_many(doc)
