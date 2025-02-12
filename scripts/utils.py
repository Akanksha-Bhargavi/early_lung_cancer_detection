import os
import json
from pymongo import MongoClient
import logging

logging.basicConfig(level=logging.INFO)

MONGO_CONFIG = {
    "host": "cluster0.xpghy.mongodb.net",      
    "port": 27017,            
    "username": "guest",  
    "password": "Guest123"  
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  
DATA_PATH = os.path.join(BASE_DIR, 'data', 'dataset.json')


URL = f"mongodb+srv://{MONGO_CONFIG['username']}:{MONGO_CONFIG['password']}@{MONGO_CONFIG['host']}/?tls=true&tlsAllowInvalidCertificates=false"

def connect_to_mongo():
    """Establish a connection to MongoDB."""
    try:
        
        client = MongoClient(URL)

        client.admin.command('ping')
        logging.info("Connected to MongoDB successfully.")
        return client
    except Exception as e:
        logging.error(f"MongoDB connection failed: {e}")
        raise e

def load_json_data(file_path):
    """Load JSON data from the specified file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        logging.info(f"Loaded data from {file_path}.")
        return data
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        raise e
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from {file_path}: {e}")
        raise e

def insert_data_to_mongo(client, data, db_name='Lungcancer', collection_name='Patients'):
    """Insert data into MongoDB collection."""
    try:
        db = client[db_name]
        collection = db[collection_name]
        result = collection.insert_many(data)
        logging.info(f"Inserted {len(result.inserted_ids)} documents into {collection_name}.")
    except Exception as e:
        logging.error(f"Failed to insert data into MongoDB: {e}")
        raise e

def get_data_from_mongo(client, db_name='Lungcancer', collection_name='Patients'):
    """Retrieve data from MongoDB and return as a DataFrame."""
    from pandas import DataFrame
    try:
        db = client[db_name]
        collection = db[collection_name]
        data_df = DataFrame(list(collection.find()))
        data_df.drop('_id', axis=1, inplace=True)  
        logging.info(f"Retrieved data from {db_name}.{collection_name}.")
        return data_df
    except Exception as e:
        logging.error(f"Failed to retrieve data from MongoDB: {e}")
        raise e

def close_mongo_connection(client):
    """Close the MongoDB connection."""
    try:
        client.close()
        logging.info("MongoDB connection closed.")
    except Exception as e:
        logging.error(f"Failed to close MongoDB connection: {e}")
        raise e

def load_data_to_mongo(client, data, db_name, collection_name):
    """Load data into a MongoDB collection."""
    try:
        db = client[db_name]
        collection = db[collection_name]
        collection.insert_many(data)
        logging.info(f"Inserted {len(data)} documents into {collection_name}.")
        return collection
    except Exception as e:
        logging.error(f"Failed to insert data into MongoDB: {e}")
        raise e
CLIENT = connect_to_mongo()
DB = CLIENT['Lungcancer']
COLLECTION = DB['Patients']