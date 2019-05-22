import pymongo
import time

myclient = pymongo.MongoClient('mongodb://106.14.150.33:27017')
mydb = myclient["test"]
mycol = mydb["commentList"]

def comment(userID, resourceID, content):
	try:
		nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		mycol.insert_one({"userID":userID, "resourceID":resourceID,"content":content,"time":nowtime})
	except pymongo.errors.DuplicateKeyError:
		return False
	return True

def findComment(resourceID):
	try:
		results = mycol.find({"resourceID" : resourceID},{ "_id" : 0 })
		if (results.count()):
			return list(results)
		return []
	except:
		return None
