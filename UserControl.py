import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']
user = mydb["user"]

def login(username,password):
	try:
		nowUser = user.find_one({"username":username})

		if (nowUser == None):
			return -100;
		if (nowUser["password"] != password):
			return -200;
		
		uid = int(nowUser["_id"]);
		return uid;
	except:
		return 0;

def register(username,password,email):
	try:
		nowid = len(user.find())+1;
		nowUser = {"_id": nowid, "username": username,"password": password};
		result = user.insert_one(nowUser);

		print(result);
		return nowid;
	except:
		return 0;