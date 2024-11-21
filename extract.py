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
        drapeau=coreData['priority']
        earliestDate=coreData['earliestDate'].strftime('%d/%m/%Y %H:%M:%S')
        
        expirationDate=coreData['expirationDate'].strftime('%d/%m/%Y %H:%M:%S')


        
    except Exception as e:
        print("Erreur lors de l'appel à searchEvents :", e)

parseCoreData(coreData)





"""
todo: fct ecrire dans csv: if None-> vide else ecrire
todo: fct drapeau to nb binaire or color name
todo: qualification data has items type interv

date solde, date charge pda datevalidation what ate they

consommes et activités?
 
evenement notification or wtvr to see 



"""