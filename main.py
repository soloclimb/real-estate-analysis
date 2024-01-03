from scripts.extract.extract import get_world_bank_resource
from scripts.load.load import insert_records

result = get_world_bank_resource(resource='efin-cagm', format='json', limit=60)
print(result)
insert_records(record_name='investment_projects', records_dct= result)