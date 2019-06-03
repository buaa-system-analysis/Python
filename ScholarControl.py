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
                cklist.insert_one({"_id": cklist.find().count() + 1,"userID":userID,"scholarID":scholarID,"email":email,"status":"unfinished"})
                return True
            return False
    except:
        return False

def getAuthentication():
    try:
        authentication = cklist.find()
        return list(authentication)
    except:
        return None

def verification(id):
    try:
        cklist.update_one({"_id": id}, {"$set": {"status": "verified"}})
        verification = cklist.find_one({"_id": id})
        user.update_one({"_id": verification['userID']}, {"$set": {"scholarID": verification['scholarID']}})
        return True
    except:
        return False
    
def addScholars(id, name, org, citation, h_index, papers, fields):
    try:
        new_Scholar = {
            "_id": id,
            "name": name,
            "email": "",
            "organization": org,
            "fields":fields,
            "citation": citation,
            "h_index": h_index,
            "g_index":0,
            "papers": papers,
            "projects":[],
            "patents":[],
            "coAuthors":[],
            "coOrgs":[]
        };
        scholar.insert_one(new_Scholar);
        return id
    except:
        return 0

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

def findScholarByKwd(kwd):
    try:
        results = scholar.find({ "$or" : [{"name" : { "$regex" : ".*" + kwd + ".*" } }, {"fields" : { "$regex" : ".*" + kwd + ".*" } }, {"organization" : { "$regex" : ".*" + kwd + ".*" } }]} )
        if results.count()>100:
            data = []
            for i in range(100):
                data.append(results.next())
            return data
        elif results.count():
            return list(results)
        return []
    except:
        return None

#print(findScholarByKwd('a'))

def deleteScholar(scholarID):
    try:
        scholar.delete_one({"_id":scholarID})
        user.update_one({"scholarID":scholarID},{"$set":{"scholarID":0}})
        return True
    except:
        return False


#print(findScholarByKwd(""))
#print(authenticate(1,1,"a222@sdf.cc"))
#print(authenticate(1,"c111@11.cc"))
# print(findScholar(1))
# print(deleteScholar(1))
