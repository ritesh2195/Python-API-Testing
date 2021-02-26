import requests

response = requests.get('https://api.github.com/user', auth=('ritesh2195', 'thtryj'))

assert response.status_code == 200
