from sodapy import Socrata
from dotenv import dotenv_values

def get_world_bank_resource(resource, format, limit):
    domain = dotenv_values(".env")['domain']
    client = Socrata(domain, None)
    return client.get(resource, content_type=format, limit=limit)
