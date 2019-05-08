import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["commentList"]

def comment(userID, resourceID, content):
    try:
        result = mycol.insert_one({"userID":userID, "resourceID":resourceID,"content":content})
    except pymongo.errors.DuplicateKeyError:
        return False
    return True

print(comment('1','2','3'))