from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace with your actual password (URL-encoded if it has special characters)
username = "pranaysainaidupalem562006"
password = "palempranaysainaidu"  # encode special chars if needed

uri = f"mongodb+srv://{username}:{password}@cluster0.nuydz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection error:", e)