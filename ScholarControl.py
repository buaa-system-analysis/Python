import re

import pymongo

myclient = pymongo.MongoClient("mongodb://106.14.150.33:27017/")
db = myclient['test']
scholar = db['scholar']
paper = db['Paper']
user = db['user']
cklist = db['checkList']


def editScholarInfo(scholarID, data):
    try:
        scholar.update_one({"_id": scholarID}, {"$set": data})
        return True
    except:
        return False

def authenticate(userID,scholarID, email):
    try:
        user_now = user.find_one({"_id":userID})
        if not user_now:
            return False
        scholar_now = scholar.find_one({"_id":scholarID})
        if not scholar_now:
            return False
        
        if len(email)>7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                cklist.insert_one({"userID":userID,"scholarID":scholarID,"email":email,"status":"unfinished"})
                return True
            return False
    except:
        return False

def addScholar(name):
    try:
        scholar_id = scholar.find().count() + 1
        new_Scholar = {
            "_id": scholar_id, 
            "name": name,
            "email": "",
            "organization":"",
            "fields":[],
            "citation":0,
            "h_index":0,
            "g_index":0,
            "papers":[],
            "projects":[],
            "patents":[],
            "coAuthors":[],
            "coOrgs":[]
        };
        scholar.insert_one(new_Scholar);
        return scholar_id
    except:
        return 0

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

def findScholarByName(name):
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


#print(findScholarByName(""))
#print(authenticate(1,1,"a222@sdf.cc"))
#print(authenticate(1,"c111@11.cc"))
# print(findScholar(1))
# print(deleteScholar(1))

