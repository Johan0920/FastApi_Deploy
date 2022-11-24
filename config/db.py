from pymongo import MongoClient

CONNECTION_STRING_DOCKER="mongodb://admin:admin@Mongo-DB:27017/"
CONNECTION_STRING_CLOUD="mongodb+srv://admin:admin@cluster0.vyjizbp.mongodb.net/TEST"
conn = MongoClient(CONNECTION_STRING_CLOUD)




