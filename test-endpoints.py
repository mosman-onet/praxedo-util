import requests
from zeep import *
from import64 import getToken

#config connexion
access_token= getToken()
session = requests.Session()
session.headers.update({"Authorization": f"Bearer {access_token}"})
transport = Transport(session=session)

#endpoint
client= Client(wsdl="https://eu7.praxedo.com/eTech/services/cxf/v6/BusinessEventManager?wsdl",transport=transport)
tableau_intervention= [633437]
""""
#cas exemple de getEvent

interventions_qualif=[631051]
interventions_preplanif=[631108]
interventions_planif=[631024]
intervention_synchro=[631111]
interventions_realisee=[631119]
interventions_validee=[631110] #631045 with cr
interventions_annulee=[631122]
#tableau_intervention= [633438]
tableau_intervention= [633437]
#options=None

options = [
    
     client.get_type("ns0:wsEntry")(key="businessEvent.populate.coreData"),
   client.get_type("ns0:wsEntry")(key="businessEvent.populate.qualificationData"),
    client.get_type("ns0:wsEntry")(key="businessEvent.populate.schedulingData"),
    client.get_type("ns0:wsEntry")(key="businessEvent.populate.completionData.fields"),
    client.get_type("ns0:wsEntry")(key="businessEvent.populate.completionData.items"),
    client.get_type("ns0:wsEntry")(key="businessEvent.populate.annotations"),
    client.get_type("ns0:wsEntry")(key="businessEvent.populate.contractData")
    client.get_type("ns0:wsEntry")(key="businessEvent.feature.status.cancelled"), 
]
#tableau_intervention= interventions_preplanif


 try:
    response = client.service.getEvents(requestedEvents=tableau_intervention, options=options)
    print("Réponse :", response)
except Exception as e:
    print("Erreur lors de l'appel à getEvents :", e) 
    
    <request>
<dateConstraints>
<dateRange>2024-02-05T18:00:00</dateRange>
<dateRange>2024-02-05T19:00:00</dateRange>
<name>validationDate</name>
</dateConstraints>
<statusConstraint>VALIDATED</statusConstraint>
<agentIdConstraint>CLB</agentIdConstraint>
</request>
    
    """
# Construction des paramètres de la requête
date_constraint = client.get_type("ns0:dateConstraint")(
    dateRange=["2016-09-21T02:00:00", "2016-11-21T19:00:00"],  # Période de date
    name= "lastModificationDate",  # Nom de la contrainte
)
#validated: validationDtae; new: creationDate,
status = ["CANCELLED", "VALIDATED", "COMPLETED", "IN_PROGRESS", "SCHEDULED", "PRE_SCHEDULED", "QUALIFIED", "NEW"]   
#status =["CANCELLED"]
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


