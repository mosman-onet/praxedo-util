from requetteAPI import getRequette

responses=getRequette("2016-09-21","2016-11-21")

response=responses[0]
interventions=response['entities']
intervention=interventions[0]


nomAgence=intervention['coreData']['referentialData']['customerName']
print(f'inter = {intervention}')