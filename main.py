from scripts.extract.extract import get_world_bank_resource
from scripts.load.load import insert_records

resource_columns = ['date_disclosed', 'project_url', 
                    'company_name', 'country', 'industry',
                    'status', 'ifc_invested_date', 
                    'ifc_investment_for_risk_management_million_usd', 
                    'ifc_investment_for_loan_million_usd', 
                    'total_ifc_investment_as_approved_by_board_million_usd', 
                    'as_of_date']

result = get_world_bank_resource(resource='efin-cagm', resourse_columns=resource_columns,  format='json', limit=60)
insert_records(record_name='investment_projects', records_dct= result)