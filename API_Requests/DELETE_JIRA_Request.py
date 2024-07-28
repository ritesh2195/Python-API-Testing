import requests

response = requests.delete('https://riteshautomation.atlassian.net/rest/api/2/issue/10036',

                           auth=('email', 'apikey'))

print(response.status_code)
