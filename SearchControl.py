import pymongo

myclient = pymongo.MongoClient("mongodb://106.14.150.33:27017/")
mydb = myclient["test"]
mycol = mydb["search"]

def search(category, keyword):
    try:
        return [{ "item" : 1, "scholar" : 1 }, { "item" : 2, "scholar" : 2 },{ "item" : 3, "scholar" : 3 }]
    except pymongo.errors.DuplicateKeyError:
        return None
