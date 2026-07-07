from pymongo import MongoClient
uri = "mongodb+srv://shreyashnagrale260_db_user:Shreyash260@mongocluster.dkbdymv.mongodb.net/?appName=MongoCluster"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)