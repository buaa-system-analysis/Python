import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']

def login(username,password):
	mycol = mydb["user"]

	x = mycol.find_one({"username":username,"password":password})

	print(x);
	if (x != None):
		return x["_id"];
	else:
		return 0;

print(login("aaa","12346"));
