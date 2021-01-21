import requests

response = requests.get('https://riteshautomation.atlassian.net/rest/api/2/issue/BAN-16',

                        auth=('riteshranjanmishra938@gmail.com', '5W4ViEe5qcxoviSN5IDY3B09'),)
assert response.status_code == 200
print(response.headers['Content-Type'])
print(response.json())
