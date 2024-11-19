import requests
from zeep import *
from import64 import getToken

def getRequette(dateModif,dateAujd):
    #config connexion
    access_token= getToken()
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {access_token}"})
    transport = Transport(session=session)

    #endpoint
    client= Client(wsdl="https://eu7.praxedo.com/eTech/services/cxf/v6/BusinessEventManager?wsdl",transport=transport)
    # Construction des paramètres de la requête
    date_constraint = client.get_type("ns0:dateConstraint")(
        dateRange=[f"{dateModif}T00:00:00", f"{dateAujd}T19:00:00"],  # Période de date
        name= "lastModificationDate",  # Nom de la contrainte
    )
    
    status = ["CANCELLED", "VALIDATED", "COMPLETED", "IN_PROGRESS", "SCHEDULED", "PRE_SCHEDULED", "QUALIFIED", "NEW"]   
    request_type = client.get_type("ns0:businessEventsRequest")
    request = request_type(
        dateConstraints=date_constraint,
        statusConstraint=status
    )

    options_type = client.get_type("ns0:wsEntry")
    options = [
        options_type(key="businessEvent.populate.coreData"),
        options_type(key="businessEvent.populate.qualificationData"),
        options_type(key="businessEvent.populate.schedulingData"),
        #options_type(key="businessEvent.populate.completionData.fields"),
        #options_type(key="businessEvent.populate.completionData.items"),
    ]
    try:
        response = client.service.searchEvents(
            request=request,  
            batchSize=1,  
            firstResultIndex=0, 
            options=options  
        )
        print("Réponse :", response)
    except Exception as e:
        print("Erreur lors de l'appel à searchEvents :", e)

getRequette("2016-09-21","2016-11-21")

""" TODO:
        boucle tant que reponse.code=200, on refait index=index+50
        recuperer reponse dans chaine de caractere
        renvoyer chaine de caractere
    
    TODO FCT ECRITURE DANS FICHIER EXCELL:

    
        """