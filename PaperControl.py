import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["purchaseList"]

def purchase(userID, paperID):
    try:
        result = mycol.insert_one({"_id":"userID", "userID":userID, "paperID":paperID})
    except pymongo.errors.DuplicateKeyError:
        return False
    return True


def download(userID, paperID):
    result = mycol.find({"userID": userID, "paperID": paperID})
    if result.count():
        mycol1 = mydb['paperList']
        result = mycol1.find({"paperID":paperID})
        if result.count():
            return result[0]['url'] # 返回下载链接 需根据paperID查找对应的
    else:
        return None


# print(purchase('1', '11'))
# print(purchase('1', '11'))
# print(purchase('22', '22'))
# print(download('1','11'))
# print(purchase('1', '33'))
# print(purchase('3', '45'))