import re

import pymongo

myclient = pymongo.MongoClient("mongodb://106.14.150.33:27017/")
db = myclient['test']
scholar = db['scholar']
paper = db['Paper']
user = db['user']


def editScholarInfo(scholarID, name, organization, resourceField):
    try:
        scholar.update_one({"_id": scholarID}, {"$set": { "name": name, "organization": organization, "resourceField": resourceField}})
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
                scholar_id = scholar.find().count() + 1
                new_Scholar = {
                    "_id": scholar_id, 
                    "name": "",
                    "email": email,
                    "organization":"",
                    "researchField":"",
                    "researchTopic":"",
                    "citation":"",
                    "pubNumber":"",
                    "h-Index":"",
                    "coAuthor":"",
                    "coOrg":""
                };
                scholar.insert_one(new_Scholar);
                user.update_one({"_id":userID},{"$set":{"scholarID":scholar_id}})
                return True
            return False
    except:
        return False

def manageResource(resourceID,cmd,newPrice):
    try:
        if(cmd == 1):
            paper.update_one({"_id":resourceID},{"$set":{"price":newPrice}})
            return True
        else:
            return False
    except:
        return False

def findScholar(scholarID):
    try:
        now_scholar = scholar.find_one({"_id":scholarID})
        return now_scholar
    except:
        return None

def findscholarByName(name):
    try:
        results = scholar.find({"name" : { "$regex" : ".*" + name + ".*" } })
        if (results.count()):
            return list(results)
        return []
    except:
        return None

def deleteScholar(scholarID):
    try:
        scholar.delete_one({"_id":scholarID})
        user.update_one({"scholarID":scholarID},{"$set":{"scholarID":0}})
        return True
    except:
        return False

#print(authenticate(1,"c111@11.cc"))
# print(findScholar(1))
# print(deleteScholar(1))

