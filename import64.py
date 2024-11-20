import base64
import requests
from zeep import *

def getToken():
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
    return access_token