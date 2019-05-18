import pymongo

 
myclient = pymongo.MongoClient('mongodb://106.14.150.33:27017')
mydb = myclient["test"]
slcol = mydb["subscribeList"] # 订阅列表，{"userID": userID, "scholarID": scholarID}
plcol = mydb['paperList'] # 论文列表，{"paperListID": paperListID, "paperID": paperID}
crlcol = mydb['createList'] # 创建的论文列表，{"userID": userID, "paperListID": paperListID}
colcol = mydb['collectionList'] # 收藏的（他人的）论文列表，{"userID": userID, "paperListID": paperListID}


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
        mydict = {"paperListID": paperListID, "paperID": paperID}
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


def searchUserid(userID):
    try:
        mydict = {"userID": userID}
        user_list = list(colcol.find(mydict))
        return user_list
    except:
        return None


def searchScholar(scholarID):
    try:
        mydict = {"scholarID": scholarID}
        scholar_list = list(slcol.find(mydict))
        return scholar_list
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
