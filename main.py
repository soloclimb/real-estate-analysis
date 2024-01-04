from scripts.extract.extract import get_world_bank_resource
from scripts.load.load import insert_records

from json import load
resourses_columns = None
with open("./config/extract-config.json", "r") as config:
    resourses_columns = load(config)

for resource in resourses_columns:
    result = get_world_bank_resource(resource='efin-cagm', resourse_columns=resourses_columns[resource],  format='json', limit=60)
    insert_records(record_name='investment_projects', records_dct= result)