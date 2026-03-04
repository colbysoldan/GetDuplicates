from CW_Wrapper.cw_api import *
import pandas as pd


# This strict pulls a list of companies with exact name matches and exports it to a csv
database = 'test'
companies, comp_response = CompaniesAPI(database).get_companies()

for company in companies:
    if company.deletedFlag:
        companies.remove(company)


companies_list = []
for company in companies:
    company_name = company.name
    company_name = company_name.rstrip()
    companies_list.append(company_name)

seen = set()
dupes = set()

for x in companies_list:
    if x in seen:
        dupes.add(x)
    else:
        seen.add(x)

# print(dupes)

dupe_companies = pd.DataFrame(dupes, columns=["Company Name"])
dupe_companies.to_csv('dup_comps.csv', index=False)