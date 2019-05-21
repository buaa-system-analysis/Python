import pymongo

myclient = pymongo.MongoClient('mongodb://106.14.150.33:27017')
mydb = myclient["test"]
mycol = mydb["purchaseList"]

def purchase(userID, paperID):
    try:
        mycol.insert_one({"_id":userID+paperID, "userID":userID, "paperID":paperID})
    except pymongo.errors.DuplicateKeyError:
        return False
    return True


def download(userID, paperID):
    result = mycol.find({"userID": userID, "paperID": paperID})
    if result.count():
        mycol1 = mydb['paperList']
        result = mycol1.find({"paperID":paperID})
        if result.count():
            return result[0]['url']
    else:
        return None


# print(purchase('1', '11'))
# print(purchase('1', '12'))
# print(purchase('1', '12'))
# print(download('1','13'))
# print(purchase('1', '33'))
# print(purchase('3', '45'))
