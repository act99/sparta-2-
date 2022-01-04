from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta2

# 코딩 시작

doc = {'name':'bobby','age':32}
db.users.insert_one(doc)

same_ages = list(db.users.find({},{'_id':False}))
for person in same_ages:
    print(person)

user = db.users.find_one({"name":"bobby"}, {"_id":False})
print(user)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

db.users.delete_one({'name':'bobby'})