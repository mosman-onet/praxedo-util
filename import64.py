import base64
import requests
from zeep import *

#getting token
client_secret = '7ErjxbFKwqlZa3UTn6iVaNbBTzvgaoZ2d30QS2GEmMkcLgbeNRl5FyCC3qa6e_wb'  
client_id = '0oaidgfjgwWnrv0G7417' 


credentials = f'{client_id}:{client_secret}'
print(f"credentiels : {credentials}")
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
print(f"credentiels : {encoded_credentials}")
url = 'https://auth.praxedo.com/oauth2/ausaua1mf29S8ptC0417/v1/token'


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {encoded_credentials}'
}

data = {
    'grant_type': 'client_credentials',
    'scope':'ws_v6'
}


response = requests.post(url, headers=headers, data=data)


token_data = response.json()
access_token = token_data.get('access_token')
print(f'Jeton d\'accès : {access_token}')

#config connexion
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
tableau_intervention= [633438]
options=None
#tableau_intervention= interventions_preplanif
try:
    response = client.service.getEvents(requestedEvents=tableau_intervention, options=options)
    print("Réponse :", response)
except Exception as e:
    print("Erreur lors de l'appel à getEvents :", e)
