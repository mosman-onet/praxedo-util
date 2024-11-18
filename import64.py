import base64
import requests

client_id = 'ausaua1mf29S8ptC0417'  
client_secret = '0oaidgfjgwWnrv0G7417' 


credentials = f'{client_id}:{client_secret}'
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

url = 'https://auth.praxedo.com/oauth2/ausaua1mf29S8ptC0417/v1/token'


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {encoded_credentials}'
}

data = {
    'grant_type': 'client_credentials'
}


response = requests.post(url, headers=headers, data=data)


if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get('access_token')
    print(f'Jeton d\'accès : {access_token}')
else:
    print(f'Erreur {response.status_code}: {response.text}')
