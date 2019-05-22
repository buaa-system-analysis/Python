import pymongo
from SearchControl import getPaperByID
from ScholarControl import findScholar

 
myclient = pymongo.MongoClient('mongodb://106.14.150.33:27017')
mydb = myclient["test"]
slcol = mydb["subscribeList"]
plcol = mydb['paperList']
crlcol = mydb['createList'] 
colcol = mydb['collectionList']

# mydict = { "userID": "00001", "scholarID": "00057"}
 
# mycol.insert_one(mydict) 

def subscribe(userID, scholarID, cmd):
	try:
		mydict = {"userID": userID, "scholarID": scholarID}
		found = slcol.find_one(mydict)
		if cmd:
			if not found:
				slcol.insert_one(mydict)
				return True
			else:
				return False
		else:
			if found:
				slcol.delete_one(mydict)
				return True
			else:
				return False
	except:
		return False		


def manageCollection(userID, paperListID, cmd, name):
	try:
		mydict = {"userID": userID, "paperListID": paperListID}
		if cmd == 1 and name == None:
			name = "defalut"
		if cmd == 1:
			plist = crlcol.find()

			pid = 1
			if (plist.count() > 0):
				plist = list(plist)
				pid = plist[len(plist)-1]["_id"] + 1
			crlcol.insert_one({"_id" : pid, "userID" : userID, "name" : name})
			return True
		elif cmd == 2:
			found = crlcol.find_one({"_id" : paperListID})
			if found:
				crlcol.delete_one({"_id" : paperListID})
				return True
			else:
				return False
		elif cmd == 3:
			found = colcol.find_one(mydict)
			if not found:
				colcol.insert_one(mydict)
				return True
			else:
				return False
		elif cmd == 4:
			found = colcol.find_one(mydict)
			if found:
				colcol.delete_one(mydict)
				return True
			else:
				return False
		else:
			return False
	except:
		return False


def collectPaper(userID, paperListID, cmd, paperID):
	try:
		if not crlcol.find_one({"userID": userID, "_id": paperListID}):
			return False
		mydict = {"paperListID": paperListID, "paperID": paperID}
		found = plcol.find_one(mydict)
		if cmd == "ADD":
			if not found:
				plcol.insert_one(mydict)
				return True
			else:
				return False
		elif cmd == "DEL":
			if found:
				plcol.delete_one(mydict)
				return True
			else:
				return False
	except:
		return False


def getPaperList(userID,paperListID):
	try:
		if (userID == 0 or userID == "0" or userID == '0'):
			results = plcol.find({"paperListID" : paperListID })

			finalresults = []
			for result in results:
				finalresults.append(getPaperByID(result["paperID"]))
			return finalresults
		elif (paperListID == 0 or paperListID == "0" or paperListID == '0'):
			data = { "mylist" : [], "collist" : [] }
			mylist = crlcol.find({"userID" : userID})
			if (mylist.count()):
				data["mylist"] = list(mylist)

			collist = colcol.find({"userID" : userID})
			for col in collist:
				fd = crlcol.find_one({"_id" : col["paperListID"]})
				if (fd != None):
					data["collist"].append(fd)
				else:
					data["collist"].append({"_id" : 0, "name" : "创建者已删除此列表"})

			return data

	except:
		return None


def getSubscribeList(userID):
	try:
		results = slcol.find({"userID": userID})

		finalresults = []
		for result in results:
			finalresults.append(findScholar(result["scholarID"]))
		return finalresults

	except:
		return None