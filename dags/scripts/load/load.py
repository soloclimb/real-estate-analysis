from pymongo.mongo_client import MongoClient
from dotenv import dotenv_values

mongo_connection_str = dotenv_values('.env')['mongo_connection_str']

def connect_to_mongodb(cnt_string):
    client = MongoClient(cnt_string)
    try:
        client.admin.command('ping')
        print(f"Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return {'db': client.get_database(), 'client': client}

def insert_records(record_name, records_dct):
    con = connect_to_mongodb(mongo_connection_str)
    db = con['db']
    client =  con['client']

    db[record_name].insert_many(records_dct)
    client.close()