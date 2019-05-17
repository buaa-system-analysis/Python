import re

import pymongo

myclient = pymongo.MongoClient("mongodb://106.14.150.33:27017/")
db = myclient['test']
scholar = db['scholar']
user = db['user']


def editScholarInfo(scholarID, name, organization, resourceField):
    try:
        scholar.update_one({"_id": scholarID}, {"$set": {
                           "name": name, "organization": organization, "resourceField": resourceField}})
        return True
    except:
        return False

def authenticate(userID, email):
    try:
        user_now = user.find_one({"_id":userID})
        if not user_now:
            return False
        if len(email)>7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                return True
            return False
    except:
        return False
