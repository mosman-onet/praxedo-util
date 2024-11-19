import base64
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

#cas exemple

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
    """client.get_type("ns0:wsEntry")(key="businessEvent.populate.completionData.fields"),
    client.get_type("ns0:wsEntry")(key="businessEvent.populate.completionData.items"),
    client.get_type("ns0:wsEntry")(key="businessEvent.populate.annotations"),
    client.get_type("ns0:wsEntry")(key="businessEvent.populate.contractData"),
    client.get_type("ns0:wsEntry")(key="businessEvent.feature.status.cancelled"), """
]
#tableau_intervention= interventions_preplanif


""" try:
    response = client.service.getEvents(requestedEvents=tableau_intervention, options=options)
    print("Réponse :", response)
except Exception as e:
    print("Erreur lors de l'appel à getEvents :", e) """

try:
    response = client.service.getEvents(requestedEvents=tableau_intervention, options=options)
    print("Réponse :", response)
except Exception as e:
    print("Erreur lors de l'appel à getEvents :", e)
