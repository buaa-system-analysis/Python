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
            found = crlcol.find_one(mydict)
            if not found:
                crlcol.insert_one(mydict)
                return True
            else:
                return False
        elif cmd == 2:
            found = crlcol.find_one(mydict)
            if found:
                crlcol.delete_one(mydict)
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
        if not crlcol.find_one({"userID": userID, "paperListID": paperListID}):
            return False
        mydict = {"userID": userID, "paperListID": paperListID, "paperID": paperID}
        found = plcol.find_one(mydict)
        if cmd:
            if not found:
                plcol.insert_one(mydict)
                return True
            else:
                return False
        else:
            if found:
                plcol.delete_one(mydict)
                return True
            else:
                return False
    except:
        return False


def getPaperList(userID,paperListID):
    try:
        results = plcol.find({"userID" : userID, "paperListID" : paperListID })

        finalresults = []
        for result in results:
        	finalresults.append(getPaperByID(result["paperID"]))
        return finalresults

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

# print("### BEFORE ###")
# for x in mycol.find():
#     print(x)

# subscribe('00001', '00057', True)
# subscribe('00001', '00057', True)

# print("### AFTER ###")
# for x in mycol.find():
#     print(x)
