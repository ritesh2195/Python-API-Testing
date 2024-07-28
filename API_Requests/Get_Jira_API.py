import requests

#response = requests.get('https://riteshautomation.atlassian.net/rest/api/2/issue/BAN-16',

#                        auth=('riteshranjanmishra938@gmail.com', '5W4ViEe5qcxoviSN5IDY3B09'), )

sc = requests.Session()

sc.auth = ('email', 'apikey')

sc.headers.update({'Content-Type': 'application/json'})

response = sc.get('https://riteshautomation.atlassian.net/rest/api/2/issue/BAN-33')

json_response = response.json()

print(type(json_response))

fields = json_response['fields']

print(type(fields['issuetype']))
print(fields['issuetype']['description'])


assert response.status_code == 200


