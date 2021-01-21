import requests

response = requests.delete('https://riteshautomation.atlassian.net/rest/api/2/issue/10036',

                           auth=('riteshranjanmishra938@gmail.com', '5W4ViEe5qcxoviSN5IDY3B09'))

print(response.status_code)
