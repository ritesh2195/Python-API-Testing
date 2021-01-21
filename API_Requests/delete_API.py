import requests

from API_Requests.payLoad import addBody, DBPayLoad
from Utilities.Configuration import getConfig
from Utilities.resources import AddResources

query = 'select * from Books'

headers = {'Content-Type': 'application/json'}

url = getConfig()['API Testing']['EndPoint'] + AddResources.AddBook

response = requests.post(url, json=DBPayLoad(query), headers=headers)

print(response.json())

response_json = response.json()

book_ID = response_json['ID']

print(book_ID)

delete_url = getConfig().get('API Testing', 'EndPoint') + AddResources.DeleteBook

response_delete = requests.post(delete_url, json={'ID': book_ID},
                                headers={'Content-Type': 'application/json'})

print(response_delete.json())


