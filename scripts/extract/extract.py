from sodapy import Socrata
from dotenv import dotenv_values

def get_world_bank_resource(resource, format, limit, resourse_columns):
    
    domain = dotenv_values(".env")['domain']
    client = Socrata(domain, None)
    return client.get(resource, query=f"SELECT {', '.join(resourse_columns)} LIMIT {limit}", content_type=format)
