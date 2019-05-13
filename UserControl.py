import pymongo
 
myclient = pymongo.MongoClient('mongodb://106.14.150.33:27017/')
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
		chkUser = user.find_one({"username":username});
		if (chkUser != None):
			return 0;

		nowid = user.find().count()+1;
		nowUser = {
			"_id": nowid, 
			"username": username,
			"password": password, 
			"email": email,
			"name" : "",
			"organization" : "",
			"introduction" : "",
			"scholarID" : 0,
			"subscribe" : [],
			"collection" : [],
			"purchased" : []
		};
		result = user.insert_one(nowUser);

		print(result);
		return nowid;
	except:
		return 0;



def find(userID):
	try:
		nowUser = user.find_one({"_id":userID});

		if not nowUser:
			return None;

		return nowUser;
	except:
		return None;

def editInfo(userID,introduction,organization):
	try:
		user.update_one({"_id":userID}, { "$set": {"introduction": introduction, "organization": organization} });

		return True;
	except:
		return False;

def changePassword(userID,oldPassword,newPassword):
	try:
		if not user.find_one({"_id":userID,"password":oldPassword}):
			return False;

		user.update_one({"_id":userID,"password":oldPassword}, { "$set": {"password":newPassword} });

		return True;
	except:
		return False;
