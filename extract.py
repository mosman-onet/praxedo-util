from pandas import to_datetime
from requetteAPI import getRequetteSansCR

responses=getRequetteSansCR("2016-09-21","2016-11-21")

response=responses[0]
interventions=response['entities']
intervention=interventions[0]


#nomAgence=intervention['coreData']['referentialData']['customerName']
print(f'inter = {intervention}')
coreData=intervention['coreData']
def parseCoreData(coreData):
    try:
        dateCreation=coreData['creationDate'].strftime('%d/%m/%Y %H:%M:%S')
        #print("date = ", dateCreation)
        description=coreData['description']
        print("date = ", description)
        drapeau=coreData['priority']

    except Exception as e:
        print("Erreur lors de l'appel à searchEvents :", e)

parseCoreData(coreData)





"""
todo: fct ecrire dans csv: if None-> vide else ecrire
fct drapeau to nb binaire or color name

"""